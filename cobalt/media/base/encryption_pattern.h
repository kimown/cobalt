// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef COBALT_MEDIA_BASE_ENCRYPTION_PATTERN_H_
#define COBALT_MEDIA_BASE_ENCRYPTION_PATTERN_H_

#include "cobalt/media/base/media_export.h"
#include "starboard/types.h"

namespace cobalt {
namespace media {

// CENC 3rd Edition adds pattern encryption, through two new protection
// schemes: 'cens' (with AES-CTR) and 'cbcs' (with AES-CBC).
// The pattern applies independently to each 'encrypted' part of the frame (as
// defined by the relevant subsample entries), and reduces further the
// actual encryption applied through a repeating pattern of (encrypt:skip)
// 16 byte blocks. For example, in a (1:9) pattern, the first block is
// encrypted, and the next nine are skipped. This pattern is applied
// repeatedly until the end of the last 16-byte block in the subsample.
// Any remaining bytes are left clear.
// If crypt_byte_block is 0, pattern encryption is disabled.
// TODO(jrummell): Use base::Optional<EncryptionPattern> everywhere, and remove
// IsInEffect().
class MEDIA_EXPORT EncryptionPattern {
 public:
  EncryptionPattern();
  EncryptionPattern(uint32_t crypt_byte_block, uint32_t skip_byte_block);
  EncryptionPattern(const EncryptionPattern& rhs);
  EncryptionPattern& operator=(const EncryptionPattern& rhs);
  ~EncryptionPattern();

  bool Matches(const EncryptionPattern& other) const;

  uint32_t crypt_byte_block() const { return crypt_byte_block_; }
  uint32_t skip_byte_block() const { return skip_byte_block_; }

  bool IsInEffect() const;

  bool operator==(const EncryptionPattern& other) const;
  bool operator!=(const EncryptionPattern& other) const;

 private:
  uint32_t crypt_byte_block_ = 0;  // Count of the encrypted blocks.
  uint32_t skip_byte_block_ = 0;   // Count of the unencrypted blocks.
};

}  // namespace media
}  // namespace cobalt

#endif  // COBALT_MEDIA_BASE_ENCRYPTION_PATTERN_H_
