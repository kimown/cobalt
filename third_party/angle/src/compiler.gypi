# Copyright (c) 2013 The ANGLE Project Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
    'variables':
    {
        'angle_translator_exported_headers':
        [
          "include/GLSLANG/ShaderLang.h",
          "include/GLSLANG/ShaderVars.h",
          "src/compiler/translator/blocklayout.h",
          "src/compiler/translator/blocklayoutHLSL.h",
        ],
        'angle_translator_sources':
        [
            '<(DEPTH)/third_party/angle/include/EGL/egl.h',
            '<(DEPTH)/third_party/angle/include/EGL/eglext.h',
            '<(DEPTH)/third_party/angle/include/EGL/eglplatform.h',
            '<(DEPTH)/third_party/angle/include/GLES2/gl2.h',
            '<(DEPTH)/third_party/angle/include/GLES2/gl2ext.h',
            '<(DEPTH)/third_party/angle/include/GLES2/gl2platform.h',
            '<(DEPTH)/third_party/angle/include/GLES3/gl3.h',
            '<(DEPTH)/third_party/angle/include/GLES3/gl3platform.h',
            '<(DEPTH)/third_party/angle/include/GLES3/gl31.h',
            '<(DEPTH)/third_party/angle/include/GLES3/gl32.h',
            '<(DEPTH)/third_party/angle/include/KHR/khrplatform.h',
            '<(DEPTH)/third_party/angle/include/angle_gl.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/BaseTypes.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/BuiltInFunctionEmulator.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/BuiltInFunctionEmulator.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/CallDAG.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/CallDAG.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/CodeGen.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/CollectVariables.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/CollectVariables.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Common.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Compiler.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Compiler.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ConstantUnion.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ConstantUnion.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Declarator.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Declarator.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Diagnostics.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Diagnostics.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/DirectiveHandler.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/DirectiveHandler.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ExtensionBehavior.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ExtensionBehavior.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/FlagStd140Structs.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/FlagStd140Structs.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/FunctionLookup.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/FunctionLookup.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/HashNames.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/HashNames.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ImmutableString.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ImmutableStringBuilder.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ImmutableStringBuilder.h',
            # TODO: Consider ImmutableString_ESSL_autogen.cpp below,
            #       see https://chromium-review.googlesource.com/c/angle/angle/+/1757372
            '<(DEPTH)/third_party/angle/src/compiler/translator/ImmutableString_autogen.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/InfoSink.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/InfoSink.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Initialize.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Initialize.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/InitializeDll.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/InitializeDll.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/InitializeGlobals.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/IntermNode.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/IntermNode.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/IsASTDepthBelowLimit.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/IsASTDepthBelowLimit.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Operator.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Operator.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputTree.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputTree.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ParseContext.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ParseContext.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ParseContext_interm.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ParseContext_complete_autogen.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ParseContext_ESSL_autogen.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/PoolAlloc.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/PoolAlloc.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Pragma.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/QualifierTypes.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/QualifierTypes.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Severity.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ShaderLang.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ShaderVars.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/StaticType.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Symbol.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Symbol.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/SymbolTable.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/SymbolTable.h',
            # TODO: Consider using SymbolTable_ESSL_autogen.cpp below,
            #       see https://chromium-review.googlesource.com/c/angle/angle/+/1757372
            '<(DEPTH)/third_party/angle/src/compiler/translator/SymbolTable_autogen.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/SymbolTable_autogen.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/SymbolUniqueId.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/SymbolUniqueId.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Types.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/Types.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateAST.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateAST.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateGlobalInitializer.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateGlobalInitializer.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateLimitations.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateLimitations.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateMaxParameters.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateMaxParameters.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateOutputs.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateOutputs.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateSwitch.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateSwitch.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateVaryingLocations.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ValidateVaryingLocations.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/VariablePacker.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/VariablePacker.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/blocklayout.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/glslang.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/glslang_lex_autogen.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/glslang_tab_autogen.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/glslang_tab_autogen.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/length_limits.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/util.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/util.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/AddAndTrueToLoopCondition.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/AddAndTrueToLoopCondition.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/BreakVariableAliasingInInnerLoops.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/BreakVariableAliasingInInnerLoops.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ClampFragDepth.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ClampFragDepth.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ClampPointSize.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ClampPointSize.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/DeclareAndInitBuiltinsForInstancedMultiview.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/DeclareAndInitBuiltinsForInstancedMultiview.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/DeferGlobalInitializers.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/DeferGlobalInitializers.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/EmulateGLFragColorBroadcast.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/EmulateGLFragColorBroadcast.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/EmulateMultiDrawShaderBuiltins.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/EmulateMultiDrawShaderBuiltins.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/EmulatePrecision.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/EmulatePrecision.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ExpandIntegerPowExpressions.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ExpandIntegerPowExpressions.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/FoldExpressions.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/FoldExpressions.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/InitializeVariables.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/InitializeVariables.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/NameEmbeddedUniformStructs.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/NameEmbeddedUniformStructs.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/NameNamelessUniformBuffers.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/NameNamelessUniformBuffers.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/PruneEmptyCases.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/PruneEmptyCases.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/PruneNoOps.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/PruneNoOps.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RecordConstantPrecision.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RecordConstantPrecision.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RegenerateStructNames.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RegenerateStructNames.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveArrayLengthMethod.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveArrayLengthMethod.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveDynamicIndexing.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveDynamicIndexing.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveInvariantDeclaration.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveInvariantDeclaration.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemovePow.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemovePow.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveUnreferencedVariables.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveUnreferencedVariables.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteAtomicCounters.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteAtomicCounters.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteAtomicFunctionExpressions.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteAtomicFunctionExpressions.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteCubeMapSamplersAs2DArray.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteCubeMapSamplersAs2DArray.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteDfdy.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteDfdy.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteDoWhile.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteDoWhile.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteExpressionsWithShaderStorageBlock.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteExpressionsWithShaderStorageBlock.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteStructSamplers.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteStructSamplers.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteStructSamplersOld.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteRepeatedAssignToSwizzled.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteRepeatedAssignToSwizzled.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteRowMajorMatrices.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteRowMajorMatrices.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteTexelFetchOffset.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteTexelFetchOffset.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteUnaryMinusOperatorFloat.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteUnaryMinusOperatorFloat.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteUnaryMinusOperatorInt.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteUnaryMinusOperatorInt.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ScalarizeVecAndMatConstructorArgs.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ScalarizeVecAndMatConstructorArgs.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SeparateDeclarations.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SeparateDeclarations.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SimplifyLoopConditions.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SimplifyLoopConditions.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SplitSequenceOperator.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SplitSequenceOperator.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/UnfoldShortCircuitAST.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/UnfoldShortCircuitAST.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/UseInterfaceBlockFields.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/UseInterfaceBlockFields.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/VectorizeVectorScalarArithmetic.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/VectorizeVectorScalarArithmetic.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/BuiltIn.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/BuiltIn_complete_autogen.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/BuiltIn_ESSL_autogen.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/FindFunction.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/FindFunction.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/FindMain.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/FindMain.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/FindSymbolNode.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/FindSymbolNode.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/IntermNodePatternMatcher.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/IntermNodePatternMatcher.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/IntermNode_util.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/IntermNode_util.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/IntermTraverse.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/IntermTraverse.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/NodeSearch.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/ReplaceVariable.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/ReplaceVariable.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/ReplaceShadowingVariables.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/ReplaceShadowingVariables.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/RunAtTheEndOfShader.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/RunAtTheEndOfShader.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_util/Visit.h',
            '<(DEPTH)/third_party/angle/src/third_party/compiler/ArrayBoundsClamper.cpp',
            '<(DEPTH)/third_party/angle/src/third_party/compiler/ArrayBoundsClamper.h',
        ],
        'angle_translator_essl_sources':
        [
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputESSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputESSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TranslatorESSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TranslatorESSL.h',
        ],
        'angle_translator_glsl_sources':
        [
            '<(DEPTH)/third_party/angle/src/compiler/translator/BuiltInFunctionEmulatorGLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/BuiltInFunctionEmulatorGLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/BuiltinsWorkaroundGLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/BuiltinsWorkaroundGLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ExtensionGLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ExtensionGLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputGLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputGLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputGLSLBase.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputGLSLBase.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TranslatorGLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TranslatorGLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/VersionGLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/VersionGLSL.h',
        ],
        'angle_translator_hlsl_sources':
        [
            '<(DEPTH)/third_party/angle/src/compiler/translator/ASTMetadataHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ASTMetadataHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/AtomicCounterFunctionHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/AtomicCounterFunctionHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/blocklayoutHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/BuiltInFunctionEmulatorHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/BuiltInFunctionEmulatorHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ResourcesHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ResourcesHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ShaderStorageBlockFunctionHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ShaderStorageBlockFunctionHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ShaderStorageBlockOutputHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ShaderStorageBlockOutputHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/StructureHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/StructureHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TextureFunctionHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TextureFunctionHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ImageFunctionHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/ImageFunctionHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TranslatorHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TranslatorHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/UtilsHLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/UtilsHLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/emulated_builtin_functions_hlsl_autogen.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/AddDefaultReturnStatements.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/AddDefaultReturnStatements.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ArrayReturnValueToOutParameter.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/ArrayReturnValueToOutParameter.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveSwitchFallThrough.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RemoveSwitchFallThrough.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteElseBlocks.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/RewriteElseBlocks.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SeparateArrayConstructorStatements.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SeparateArrayConstructorStatements.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SeparateArrayInitialization.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SeparateArrayInitialization.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SeparateExpressionsReturningArrays.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/SeparateExpressionsReturningArrays.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/UnfoldShortCircuitToIf.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/UnfoldShortCircuitToIf.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/WrapSwitchStatementsInBlocks.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/tree_ops/WrapSwitchStatementsInBlocks.h',
        ],
        'angle_translator_lib_vulkan_sources':
        [
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputVulkanGLSL.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/OutputVulkanGLSL.h',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TranslatorVulkan.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/translator/TranslatorVulkan.h',
        ],
        'angle_preprocessor_sources':
        [
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/DiagnosticsBase.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/DiagnosticsBase.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/DirectiveHandlerBase.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/DirectiveHandlerBase.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/DirectiveParser.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/DirectiveParser.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/ExpressionParser.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Input.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Input.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Lexer.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Lexer.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Macro.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Macro.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/MacroExpander.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/MacroExpander.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/preprocessor_lex_autogen.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/preprocessor_tab_autogen.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Preprocessor.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Preprocessor.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/SourceLocation.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Token.cpp',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Token.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/Tokenizer.h',
            '<(DEPTH)/third_party/angle/src/compiler/preprocessor/numeric_lex.h',
        ],
    },
    # Everything below this is duplicated in the GN build. If you change
    # anything also change angle/BUILD.gn
    'targets':
    [
        {
            'target_name': 'preprocessor',
            'type': 'static_library',
            'dependencies': [ 'angle_common' ],
            'includes': [ '../gyp/common_defines.gypi', ],
            'sources': [ '<@(angle_preprocessor_sources)', ],
            'msvs_settings':
            {
                  'VCCLCompilerTool':
                  {
                        'WarnAsError': 'false',
                  },
            },
        },
        {
            'target_name': 'translator',
            'type': 'static_library',
            'dependencies': [ 'preprocessor', 'angle_common' ],
            'includes': [ '../gyp/common_defines.gypi', ],
            'include_dirs':
            [
                '<(DEPTH)/third_party/angle/include',
                '<(DEPTH)/third_party/angle/src',
            ],
            'sources':
            [
                '<@(angle_translator_sources)',
            ],
            'msvs_settings':
            {
                  'VCCLCompilerTool':
                  {
                        'WarnAsError': 'false',
                  },
                  'VCLibrarianTool':
                  {
                        'AdditionalOptions': ['/ignore:4221'],
                  },
            },
            'conditions':
            [
                ['angle_enable_essl==1',
                {
                    'defines':
                    [
                        'ANGLE_ENABLE_ESSL',
                    ],
                    'direct_dependent_settings':
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_ESSL',
                        ],
                    },
                    'sources':
                    [
                        '<@(angle_translator_essl_sources)',
                    ],
                }],
                ['angle_enable_glsl==1',
                {
                    'defines':
                    [
                        'ANGLE_ENABLE_GLSL',
                    ],
                    'direct_dependent_settings':
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_GLSL',
                        ],
                    },
                    'sources':
                    [
                        '<@(angle_translator_glsl_sources)',
                    ],
                }],
                ['angle_enable_hlsl==1',
                {
                    'defines':
                    [
                        'ANGLE_ENABLE_HLSL',
                    ],
                    'direct_dependent_settings':
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_HLSL',
                        ],
                    },
                    'sources':
                    [
                        '<@(angle_translator_hlsl_sources)',
                    ],
                }],
                ['angle_enable_vulkan==1',
                {
                    'defines':
                    [
                        'ANGLE_ENABLE_VULKAN',
                    ],
                    'direct_dependent_settings':
                    {
                        'defines':
                        [
                            'ANGLE_ENABLE_VULKAN',
                        ],
                    },
                    'sources':
                    [
                        '<@(angle_translator_lib_vulkan_sources)',
                    ],
                }],
            ],
        },
    ],
}
