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

{
  'variables': {
    'variables': {
      'sb_evergreen_compatible': 1,
      'sb_evergreen_compatible_libunwind': 1,
    },
  },

  'target_defaults': {
    'default_configuration': 'raspi-2-sbversion-13_debug',
    'configurations': {
      'raspi-2-sbversion-13_debug': {
        'inherit_from': ['debug_base'],
      },
      'raspi-2-sbversion-13_devel': {
        'inherit_from': ['devel_base'],
      },
      'raspi-2-sbversion-13_qa': {
        'inherit_from': ['qa_base'],
      },
      'raspi-2-sbversion-13_gold': {
        'inherit_from': ['gold_base'],
      },
    }, # end of configurations
  },

  'includes': [
    '<(DEPTH)/starboard/raspi/2/architecture.gypi',
    '<(DEPTH)/starboard/raspi/shared/gyp_configuration.gypi',
  ],
}
