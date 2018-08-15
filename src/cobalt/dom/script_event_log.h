// Copyright 2018 The Cobalt Authors. All Rights Reserved.
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

#ifndef COBALT_DOM_SCRIPT_EVENT_LOG_H_
#define COBALT_DOM_SCRIPT_EVENT_LOG_H_

#include "base/lazy_instance.h"
#include "cobalt/base/user_log.h"
#include "cobalt/dom/event.h"

namespace cobalt {
namespace dom {

// This class records the nested events and manages the user log information.
class ScriptEventLog {
 public:
  ScriptEventLog();
  ~ScriptEventLog();
  void PushEvent(Event* event);
  void PopEvent();

 private:
  static const size_t kLogEntryMaxLength = 64;
  int current_stack_depth_;
  char event_log_stack_[base::UserLog::kEventStackMaxDepth][kLogEntryMaxLength];

  DISALLOW_COPY_AND_ASSIGN(ScriptEventLog);
};

extern base::LazyInstance<ScriptEventLog> script_event_log;

}  // namespace dom
}  // namespace cobalt

#endif  // COBALT_DOM_SCRIPT_EVENT_LOG_H_