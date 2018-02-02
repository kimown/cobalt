// This file was GENERATED by command:
//     pump.py union_type_conversion_forward.h.pump
// DO NOT EDIT BY HAND!!!


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

#ifndef COBALT_SCRIPT_V8C_UNION_TYPE_CONVERSION_FORWARD_H_
#define COBALT_SCRIPT_V8C_UNION_TYPE_CONVERSION_FORWARD_H_

#include "cobalt/script/union_type.h"
#include "cobalt/script/v8c/type_traits.h"
#include "cobalt/script/v8c/v8c_exception_state.h"
#include "cobalt/script/v8c/v8c_user_object_holder.h"
#include "cobalt/script/v8c/v8c_value_handle.h"

// Forward declaration for ToJSValue and FromJSValue for IDL union types.

namespace cobalt {
namespace script {
namespace v8c {

template <typename T1, typename T2>
void ToJSValue(v8::Isolate* isolate, const script::UnionType2<T1, T2>& in_union,
               v8::Local<v8::Value>* out_value);

template <typename T1, typename T2>
void FromJSValue(v8::Isolate* isolate, v8::Local<v8::Value> value,
                 int conversion_flags, ExceptionState* exception_state,
                 script::UnionType2<T1, T2>* out_union);

template <typename T1, typename T2, typename T3>
void ToJSValue(v8::Isolate* isolate,
               const script::UnionType3<T1, T2, T3>& in_union,
               v8::Local<v8::Value>* out_value);

template <typename T1, typename T2, typename T3>
void FromJSValue(v8::Isolate* isolate, v8::Local<v8::Value> value,
                 int conversion_flags, ExceptionState* exception_state,
                 script::UnionType3<T1, T2, T3>* out_union);

template <typename T1, typename T2, typename T3, typename T4>
void ToJSValue(v8::Isolate* isolate,
               const script::UnionType4<T1, T2, T3, T4>& in_union,
               v8::Local<v8::Value>* out_value);

template <typename T1, typename T2, typename T3, typename T4>
void FromJSValue(v8::Isolate* isolate, v8::Local<v8::Value> value,
                 int conversion_flags, ExceptionState* exception_state,
                 script::UnionType4<T1, T2, T3, T4>* out_union);

}  // namespace v8c
}  // namespace script
}  // namespace cobalt

#endif  // COBALT_SCRIPT_V8C_UNION_TYPE_CONVERSION_FORWARD_H_