# Copyright 2021 The Cobalt Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This file contains a mapping of platform names to paths to the platforms's
implementation. To add another platform, simply add another entry in the same
style to this dictionary.
"""

import sys

PLATFORMS = {
    'stub': 'starboard/stub',
    'linux-x64x11': 'starboard/linux/x64x11',
    'linux-x64x11-egl': 'starboard/linux/x64x11/egl',
    'linux-x64x11-skia': 'starboard/linux/x64x11/skia',
    'linux-x64x11-clang-crosstool': 'starboard/linux/x64x11/clang/crosstool',
    'android-arm': 'starboard/android/arm',
    'android-arm64': 'starboard/android/arm64',
    'android-arm64-vulkan': 'starboard/android/arm64/vulkan',
    'android-x86': 'starboard/android/x86',
    'raspi-2': 'starboard/raspi/2',
    'raspi-2-skia': 'starboard/raspi/2/skia',
    'evergreen-x64': 'starboard/evergreen/x64',
    'evergreen-arm-hardfp': 'starboard/evergreen/arm/hardfp',
    'evergreen-arm-softfp': 'starboard/evergreen/arm/softfp',
}

if __name__ == '__main__':
  if len(sys.argv) != 2:
    raise TypeError('Usage: {} <platform_name>'.format(sys.argv[0]))
  print(PLATFORMS[sys.argv[1]])
