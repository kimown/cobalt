// Copyright 2017 Google Inc. All Rights Reserved.
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

#include "starboard/thread.h"

#include <process.h>
#include <memory>

#include "starboard/log.h"
#include "starboard/once.h"
#include "starboard/shared/win32/thread_private.h"
#include "starboard/shared/win32/wchar_utils.h"

using starboard::shared::win32::GetThreadSubsystemSingleton;
using starboard::shared::win32::SbThreadPrivate;
using starboard::shared::win32::ThreadSubsystemSingleton;
using starboard::shared::win32::wchar_tToUTF8;

namespace {

void ResetWinError() {
  SetLastError(0);
}

// Checks for system errors and logs a human-readable error if GetLastError()
// returns an error code. Noops on non-debug builds.
void DebugLogWinError() {
#if defined(_DEBUG)
  DWORD error_code = GetLastError();
  if (!error_code)
    return;

  LPWSTR error_message;
  HRESULT hresult = HRESULT_FROM_WIN32(error_code);
  int message_size = FormatMessage(
      FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_ALLOCATE_BUFFER |
          FORMAT_MESSAGE_IGNORE_INSERTS,
      nullptr,  // Unused with FORMAT_MESSAGE_FROM_SYSTEM.
      hresult, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT),
      (LPTSTR)&error_message,
      0,  // Minimum size for output buffer.
      nullptr);
  SB_DCHECK(message_size);
  SB_LOG(ERROR) << wchar_tToUTF8(error_message);
  LocalFree(error_message);
#endif  // defined(_DEBUG)
}

class ThreadCreateInfo {
 public:
  SbThreadPrivate thread_private_;
  SbThreadEntryPoint entry_point_;
  void* user_context_;
  std::string name_;
};

void CallThreadLocalDestructors() {
  ThreadSubsystemSingleton* singleton = GetThreadSubsystemSingleton();

  // TODO note that the implementation below holds a global lock
  // while processing TLS destructors on thread exit. This could
  // be a bottleneck in some scenarios. A lockless approach may be preferrable.
  SbMutexAcquire(&singleton->mutex_);
  for (auto it = singleton->thread_local_keys_.begin();
       it != singleton->thread_local_keys_.end(); ++it) {
    if (!it->second->destructor) {
      continue;
    }
    void* entry = SbThreadGetLocalValue(it->second);
    if (!entry) {
      continue;
    }
    it->second->destructor(entry);
  }
  SbMutexRelease(&singleton->mutex_);
}

unsigned ThreadTrampoline(void* thread_create_info_context) {
  std::unique_ptr<ThreadCreateInfo> info(
      static_cast<ThreadCreateInfo*>(thread_create_info_context));

  ThreadSubsystemSingleton* singleton = GetThreadSubsystemSingleton();

  SbThreadSetLocalValue(singleton->thread_private_key_, &info->thread_private_);

  SbThreadSetName(info->name_.c_str());

  void* result = info->entry_point_(info->user_context_);

  CallThreadLocalDestructors();

  SbMutexAcquire(&info->thread_private_.mutex_);
  info->thread_private_.result_ = result;
  info->thread_private_.result_is_valid_ = true;
  SbConditionVariableSignal(&info->thread_private_.condition_);
  while (info->thread_private_.wait_for_join_) {
    SbConditionVariableWait(&info->thread_private_.condition_,
                            &info->thread_private_.mutex_);
  }
  SbMutexRelease(&info->thread_private_.mutex_);

  return 0;
}

int SbThreadPriorityToWin32Priority(SbThreadPriority priority) {
  switch (priority) {
    case kSbThreadPriorityLowest:
      return THREAD_PRIORITY_LOWEST;
    case kSbThreadPriorityLow:
      return THREAD_PRIORITY_BELOW_NORMAL;
    case kSbThreadPriorityNormal:
    case kSbThreadNoPriority:
      return THREAD_PRIORITY_NORMAL;
    case kSbThreadPriorityHigh:
      return THREAD_PRIORITY_ABOVE_NORMAL;
    case kSbThreadPriorityHighest:
    case kSbThreadPriorityRealTime:
      return THREAD_PRIORITY_HIGHEST;
  }
  SB_NOTREACHED() << "Invalid priority " << priority;
  return 0;
}
}  // namespace

SbThread SbThreadCreate(int64_t stack_size,
                        SbThreadPriority priority,
                        SbThreadAffinity affinity,
                        bool joinable,
                        const char* name,
                        SbThreadEntryPoint entry_point,
                        void* context) {
  if (entry_point == NULL) {
    return kSbThreadInvalid;
  }
  ThreadCreateInfo* info = new ThreadCreateInfo();

  info->entry_point_ = entry_point;
  info->user_context_ = context;
  info->thread_private_.wait_for_join_ = joinable;
  if (name) {
    info->name_ = name;
  }

  // Create the thread suspended, and then resume once ThreadCreateInfo::handle_
  // has been set, so that it's alway valid in the ThreadCreateInfo
  // destructor.
  uintptr_t handle =
      _beginthreadex(NULL, static_cast<unsigned int>(stack_size),
                     ThreadTrampoline, info, CREATE_SUSPENDED, NULL);
  SB_DCHECK(handle);
  info->thread_private_.handle_ = reinterpret_cast<HANDLE>(handle);
  ResetWinError();
  if (affinity != kSbThreadNoAffinity &&
      !SetThreadAffinityMask(info->thread_private_.handle_,
                             static_cast<DWORD_PTR>(affinity)) &&
      !GetLastError()) {
    SB_LOG(ERROR) << "Failed to set affinity for thread " << (name ? name : "")
                  << ". Attempted to set affinity to: " << affinity;
    DebugLogWinError();
  }
  ResetWinError();
  if (priority != kSbThreadNoPriority &&
      !SetThreadPriority(info->thread_private_.handle_,
                         SbThreadPriorityToWin32Priority(priority)) &&
      !GetLastError()) {
    SB_LOG(ERROR) << "Failed to set priority for thread " << (name ? name : "")
                  << " to " << priority;
    DebugLogWinError();
  }

  ResumeThread(info->thread_private_.handle_);

  return &info->thread_private_;
}