// Copyright 2016 Google Inc. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "starboard/microphone.h"
#include "testing/gtest/include/gtest/gtest.h"

namespace starboard {
namespace nplb {

#if SB_HAS(MICROPHONE) && SB_VERSION(2)

TEST(SbMicrophoneGetSpeechApiKeyTest, SunnyDay) {
  const char* speech_api_key = SbMicrophoneGetSpeechApiKey();

  ASSERT_NE(speech_api_key, static_cast<const char*>(NULL));
  EXPECT_NE(speech_api_key[0], '\0');
}

#endif  // SB_HAS(MICROPHONE) && SB_VERSION(2)

}  // namespace nplb
}  // namespace starboard