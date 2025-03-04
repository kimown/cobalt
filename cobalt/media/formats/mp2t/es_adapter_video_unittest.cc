// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <sstream>
#include <string>
#include <vector>

#include "base/bind.h"
#include "base/logging.h"
#include "base/macros.h"
#include "base/strings/string_util.h"
#include "base/time/time.h"
#include "cobalt/media/base/media_util.h"
#include "cobalt/media/base/stream_parser_buffer.h"
#include "cobalt/media/base/timestamp_constants.h"
#include "cobalt/media/base/video_decoder_config.h"
#include "cobalt/media/formats/mp2t/es_adapter_video.h"
#include "starboard/types.h"
#include "testing/gtest/include/gtest/gtest.h"

namespace cobalt {
namespace media {
namespace mp2t {

namespace {

VideoDecoderConfig CreateFakeVideoConfig() {
  math::Size coded_size(320, 240);
  math::Rect visible_rect(0, 0, 320, 240);
  math::Size natural_size(320, 240);
  return VideoDecoderConfig(kCodecH264, H264PROFILE_MAIN, PIXEL_FORMAT_I420,
                            COLOR_SPACE_UNSPECIFIED, coded_size, visible_rect,
                            natural_size, EmptyExtraData(), Unencrypted());
}

StreamParserBuffer::BufferQueue GenerateFakeBuffers(const int* frame_pts_ms,
                                                    const bool* is_key_frame,
                                                    size_t frame_count) {
  uint8_t dummy_buffer[] = {0, 0, 0, 0};

  StreamParserBuffer::BufferQueue buffers(frame_count);
  for (size_t k = 0; k < frame_count; k++) {
    buffers[k] =
        StreamParserBuffer::CopyFrom(dummy_buffer, arraysize(dummy_buffer),
                                     is_key_frame[k], DemuxerStream::VIDEO, 0);
    ASSERT_TRUE(buffers[k]);
    if (frame_pts_ms[k] < 0) {
      buffers[k]->set_timestamp(kNoTimestamp);
    } else {
      buffers[k]->set_timestamp(
          base::TimeDelta::FromMilliseconds(frame_pts_ms[k]));
    }
  }
  return buffers;
}

}  // namespace

class EsAdapterVideoTest : public testing::Test {
 public:
  EsAdapterVideoTest();

 protected:
  // Feed the ES adapter with the buffers from |buffer_queue|.
  // Return the durations computed by the ES adapter as well as
  // whether each frame emitted by the adapter is a key frame.
  std::string RunAdapterTest(const StreamParser::BufferQueue& buffer_queue);

 private:
  void OnNewConfig(const VideoDecoderConfig& video_config);
  void OnNewBuffer(scoped_refptr<StreamParserBuffer> buffer);

  EsAdapterVideo es_adapter_;

  std::stringstream buffer_descriptors_;

  DISALLOW_COPY_AND_ASSIGN(EsAdapterVideoTest);
};

EsAdapterVideoTest::EsAdapterVideoTest()
    : es_adapter_(
          base::Bind(&EsAdapterVideoTest::OnNewConfig, base::Unretained(this)),
          base::Bind(&EsAdapterVideoTest::OnNewBuffer,
                     base::Unretained(this))) {}

void EsAdapterVideoTest::OnNewConfig(const VideoDecoderConfig& video_config) {}

void EsAdapterVideoTest::OnNewBuffer(scoped_refptr<StreamParserBuffer> buffer) {
  buffer_descriptors_ << "(" << buffer->duration().InMilliseconds() << ","
                      << (buffer->is_key_frame() ? "Y" : "N") << ") ";
}

std::string EsAdapterVideoTest::RunAdapterTest(
    const StreamParserBuffer::BufferQueue& buffer_queue) {
  buffer_descriptors_.clear();

  es_adapter_.OnConfigChanged(CreateFakeVideoConfig());
  for (StreamParserBuffer::BufferQueue::const_iterator it =
           buffer_queue.begin();
       it != buffer_queue.end(); ++it) {
    es_adapter_.OnNewBuffer(*it);
  }
  es_adapter_.Flush();

  std::string s = buffer_descriptors_.str();
  base::TrimWhitespaceASCII(s, base::TRIM_ALL, &s);
  return s;
}

TEST_F(EsAdapterVideoTest, FrameDurationSimpleGop) {
  // PTS for a GOP without B frames - strictly increasing.
  int pts_ms[] = {30, 31, 33, 36, 40, 45, 51, 58};
  bool is_key_frame[] = {true, false, false, false, false, false, false, false};
  StreamParserBuffer::BufferQueue buffer_queue =
      GenerateFakeBuffers(pts_ms, is_key_frame, arraysize(pts_ms));

  EXPECT_EQ("(1,Y) (2,N) (3,N) (4,N) (5,N) (6,N) (7,N) (7,N)",
            RunAdapterTest(buffer_queue));
}

TEST_F(EsAdapterVideoTest, FrameDurationComplexGop) {
  // PTS for a GOP with B frames.
  int pts_ms[] = {30, 120, 60, 90, 210, 150, 180, 300, 240, 270};
  bool is_key_frame[] = {true,  false, false, false, false,
                         false, false, false, false, false};
  StreamParserBuffer::BufferQueue buffer_queue =
      GenerateFakeBuffers(pts_ms, is_key_frame, arraysize(pts_ms));

  EXPECT_EQ(
      "(30,Y) (30,N) (30,N) (30,N) (30,N) "
      "(30,N) (30,N) (30,N) (30,N) (30,N)",
      RunAdapterTest(buffer_queue));
}

TEST_F(EsAdapterVideoTest, LeadingNonKeyFrames) {
  int pts_ms[] = {30, 40, 50, 120, 150, 180};
  bool is_key_frame[] = {false, false, false, true, false, false};
  StreamParserBuffer::BufferQueue buffer_queue =
      GenerateFakeBuffers(pts_ms, is_key_frame, arraysize(pts_ms));

  EXPECT_EQ("(30,Y) (30,Y) (30,Y) (30,Y) (30,N) (30,N)",
            RunAdapterTest(buffer_queue));
}

TEST_F(EsAdapterVideoTest, LeadingKeyFrameWithNoTimestamp) {
  int pts_ms[] = {-1, 40, 50, 120, 150, 180};
  bool is_key_frame[] = {true, false, false, true, false, false};
  StreamParserBuffer::BufferQueue buffer_queue =
      GenerateFakeBuffers(pts_ms, is_key_frame, arraysize(pts_ms));

  EXPECT_EQ("(40,Y) (40,Y) (30,Y) (30,N) (30,N)", RunAdapterTest(buffer_queue));
}

TEST_F(EsAdapterVideoTest, LeadingFramesWithNoTimestamp) {
  int pts_ms[] = {-1, -1, 50, 120, 150, 180};
  bool is_key_frame[] = {false, false, false, true, false, false};
  StreamParserBuffer::BufferQueue buffer_queue =
      GenerateFakeBuffers(pts_ms, is_key_frame, arraysize(pts_ms));

  EXPECT_EQ("(70,Y) (30,Y) (30,N) (30,N)", RunAdapterTest(buffer_queue));
}

}  // namespace mp2t
}  // namespace media
}  // namespace cobalt
