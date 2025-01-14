/*
 * Copyright 2010 Google Inc.
 *
 * Use of this source code is governed by a BSD-style license that can be
 * found in the LICENSE file.
 */

#ifndef SkStrikeCache_DEFINED
#define SkStrikeCache_DEFINED

#include <unordered_map>
#include <unordered_set>

#include "include/private/SkSpinlock.h"
#include "include/private/SkTemplates.h"
#include "src/core/SkDescriptor.h"
#include "src/core/SkScalerCache.h"

class SkTraceMemoryDump;

#ifndef SK_DEFAULT_FONT_CACHE_COUNT_LIMIT
    #define SK_DEFAULT_FONT_CACHE_COUNT_LIMIT   2048
#endif

#ifndef SK_DEFAULT_FONT_CACHE_LIMIT
    #define SK_DEFAULT_FONT_CACHE_LIMIT     (2 * 1024 * 1024)
#endif

///////////////////////////////////////////////////////////////////////////////

class SkStrikePinner {
public:
    virtual ~SkStrikePinner() = default;
    virtual bool canDelete() = 0;
};

class SkStrikeCache final : public SkStrikeForGPUCacheInterface {
public:
    SkStrikeCache() = default;

    class Strike final : public SkRefCnt, public SkStrikeForGPU {
    public:
        Strike(SkStrikeCache* strikeCache,
               const SkDescriptor& desc,
               std::unique_ptr<SkScalerContext> scaler,
               const SkFontMetrics* metrics,
               std::unique_ptr<SkStrikePinner> pinner)
                : fStrikeCache{strikeCache}
                , fScalerCache{desc, std::move(scaler), metrics}
                , fPinner{std::move(pinner)} {}

        SkGlyph* mergeGlyphAndImage(SkPackedGlyphID toID, const SkGlyph& from) {
            auto [glyph, increase] = fScalerCache.mergeGlyphAndImage(toID, from);
            this->updateDelta(increase);
            return glyph;
        }

        const SkPath* mergePath(SkGlyph* glyph, const SkPath* path, bool hairline) {
            auto [glyphPath, increase] = fScalerCache.mergePath(glyph, path, hairline);
            this->updateDelta(increase);
            return glyphPath;
        }

        SkScalerContext* getScalerContext() const {
            return fScalerCache.getScalerContext();
        }

        void findIntercepts(const SkScalar bounds[2], SkScalar scale, SkScalar xPos,
                            SkGlyph* glyph, SkScalar* array, int* count) {
            fScalerCache.findIntercepts(bounds, scale, xPos, glyph, array, count);
        }

        const SkFontMetrics& getFontMetrics() const {
            return fScalerCache.getFontMetrics();
        }

        SkSpan<const SkGlyph*> metrics(SkSpan<const SkGlyphID> glyphIDs,
                                       const SkGlyph* results[]) {
            auto [glyphs, increase] = fScalerCache.metrics(glyphIDs, results);
            this->updateDelta(increase);
            return glyphs;
        }

        SkSpan<const SkGlyph*> preparePaths(SkSpan<const SkGlyphID> glyphIDs,
                                            const SkGlyph* results[]) {
            auto [glyphs, increase] = fScalerCache.preparePaths(glyphIDs, results);
            this->updateDelta(increase);
            return glyphs;
        }

        SkSpan<const SkGlyph*> prepareImages(SkSpan<const SkPackedGlyphID> glyphIDs,
                                             const SkGlyph* results[]) {
            auto [glyphs, increase] = fScalerCache.prepareImages(glyphIDs, results);
            this->updateDelta(increase);
            return glyphs;
        }

        void prepareForDrawingMasksCPU(SkDrawableGlyphBuffer* drawables) {
            size_t increase = fScalerCache.prepareForDrawingMasksCPU(drawables);
            this->updateDelta(increase);
        }

        const SkGlyphPositionRoundingSpec& roundingSpec() const override {
            return fScalerCache.roundingSpec();
        }

        const SkDescriptor& getDescriptor() const override {
            return fScalerCache.getDescriptor();
        }

        void prepareForMaskDrawing(
                SkDrawableGlyphBuffer* drawbles, SkSourceGlyphBuffer* rejects) override {
            size_t increase = fScalerCache.prepareForMaskDrawing(drawbles, rejects);
            this->updateDelta(increase);
        }

        void prepareForSDFTDrawing(
                SkDrawableGlyphBuffer* drawbles, SkSourceGlyphBuffer* rejects) override {
            size_t increase = fScalerCache.prepareForSDFTDrawing(drawbles, rejects);
            this->updateDelta(increase);
        }

        void prepareForPathDrawing(
                SkDrawableGlyphBuffer* drawbles, SkSourceGlyphBuffer* rejects) override {
            size_t increase = fScalerCache.prepareForPathDrawing(drawbles, rejects);
            this->updateDelta(increase);
        }

        void onAboutToExitScope() override {
            this->unref();
        }

        void updateDelta(size_t increase);

        SkStrikeCache* const            fStrikeCache;
        Strike*                         fNext{nullptr};
        Strike*                         fPrev{nullptr};
        SkScalerCache                   fScalerCache;
        std::unique_ptr<SkStrikePinner> fPinner;
        size_t                          fMemoryUsed{sizeof(SkScalerCache)};
        bool                            fRemoved{false};
    };  // Strike

    static SkStrikeCache* GlobalStrikeCache();

    sk_sp<Strike> findStrike(const SkDescriptor& desc) SK_EXCLUDES(fLock);

    sk_sp<Strike> createStrike(
            const SkDescriptor& desc,
            std::unique_ptr<SkScalerContext> scaler,
            SkFontMetrics* maybeMetrics = nullptr,
            std::unique_ptr<SkStrikePinner> = nullptr) SK_EXCLUDES(fLock);

    sk_sp<Strike> findOrCreateStrike(
            const SkDescriptor& desc,
            const SkScalerContextEffects& effects,
            const SkTypeface& typeface) SK_EXCLUDES(fLock);

    SkScopedStrikeForGPU findOrCreateScopedStrike(
            const SkDescriptor& desc,
            const SkScalerContextEffects& effects,
            const SkTypeface& typeface) override SK_EXCLUDES(fLock);

    static void PurgeAll();
    static void Dump();

    // Dump memory usage statistics of all the attaches caches in the process using the
    // SkTraceMemoryDump interface.
    static void DumpMemoryStatistics(SkTraceMemoryDump* dump);

    void purgeAll() SK_EXCLUDES(fLock); // does not change budget

    int getCacheCountLimit() const SK_EXCLUDES(fLock);
    int setCacheCountLimit(int limit) SK_EXCLUDES(fLock);
    int getCacheCountUsed() const SK_EXCLUDES(fLock);

    size_t getCacheSizeLimit() const SK_EXCLUDES(fLock);
    size_t setCacheSizeLimit(size_t limit) SK_EXCLUDES(fLock);
    size_t getTotalMemoryUsed() const SK_EXCLUDES(fLock);

private:
    sk_sp<Strike> internalFindStrikeOrNull(const SkDescriptor& desc) SK_REQUIRES(fLock);
    sk_sp<Strike> internalCreateStrike(
            const SkDescriptor& desc,
            std::unique_ptr<SkScalerContext> scaler,
            SkFontMetrics* maybeMetrics = nullptr,
            std::unique_ptr<SkStrikePinner> = nullptr) SK_REQUIRES(fLock);

    // The following methods can only be called when mutex is already held.
    void internalRemoveStrike(Strike* strike) SK_REQUIRES(fLock);
    void internalAttachToHead(sk_sp<Strike> strike) SK_REQUIRES(fLock);

    // Checkout budgets, modulated by the specified min-bytes-needed-to-purge,
    // and attempt to purge caches to match.
    // Returns number of bytes freed.
    size_t internalPurge(size_t minBytesNeeded = 0) SK_REQUIRES(fLock);

    // A simple accounting of what each glyph cache reports and the strike cache total.
    void validate() const SK_REQUIRES(fLock);

    void forEachStrike(std::function<void(const Strike&)> visitor) const SK_EXCLUDES(fLock);

    mutable SkMutex fLock;
    Strike* fHead SK_GUARDED_BY(fLock) {nullptr};
    Strike* fTail SK_GUARDED_BY(fLock) {nullptr};
    struct StrikeTraits {
        static const SkDescriptor& GetKey(const sk_sp<Strike>& strike) {
            return strike->getDescriptor();
        }
        static uint32_t Hash(const SkDescriptor& descriptor) {
            return descriptor.getChecksum();
        }
    };
    SkTHashTable<sk_sp<Strike>, SkDescriptor, StrikeTraits> fStrikeLookup SK_GUARDED_BY(fLock);

    size_t  fCacheSizeLimit{SK_DEFAULT_FONT_CACHE_LIMIT};
    size_t  fTotalMemoryUsed SK_GUARDED_BY(fLock) {0};
    int32_t fCacheCountLimit{SK_DEFAULT_FONT_CACHE_COUNT_LIMIT};
    int32_t fCacheCount SK_GUARDED_BY(fLock) {0};
};

using SkStrike = SkStrikeCache::Strike;

#endif  // SkStrikeCache_DEFINED
