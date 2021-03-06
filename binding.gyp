{
    "targets": [{
        "defines": [
            'NAPI_EXPERIMENTAL', 'NAPI_VERSION=5'
        ],
        # 'cflags': [ '-Wall', '-Werr', '-g' ],
        # 'ccflags': [ '-Wall', '-Werr', '-g' ],
        "target_name": "leveldown",
        "conditions": [
            ["OS == 'win'", {
                "defines": [
                    "_HAS_EXCEPTIONS=1", "OS_WIN=1"
                ], "msvs_settings": {
                    "VCCLCompilerTool": {
                        "RuntimeTypeInfo": "false", "EnableFunctionLevelLinking": "true", "ExceptionHandling": "2", "DisableSpecificWarnings": ["4355", "4530", "4267", "4244", "4506"]
                    }, 'VCLinkerTool': {
                        'AdditionalDependencies': [
                            # SDK import libs.
                            'Shlwapi.lib',
                            'rpcrt4.lib'
                        ]
                    }
                }
            }, {  # OS != 'win'
                'cflags!': ['-fno-rtti'], 'cflags_cc!': ['-fno-rtti'], 'cflags_cc+': ['-frtti']
            }], ["OS == 'mac'", {
                'xcode_settings': {
                    'WARNING_CFLAGS': [
                        '-Wno-sign-compare', '-Wno-unused-variable', '-Wno-unused-function', '-Wno-ignored-qualifiers', '-Wno-c++14-extensions', '-Wno-c++17-extensions'
                    ],
                    'OTHER_CPLUSPLUSFLAGS': [
                        '-mmacosx-version-min=10.8',
                        '-std=c++11',
                        '-stdlib=libc++'
                    ],
                    'OTHER_LDFLAGS': ['-stdlib=libc++'],
                    'GCC_ENABLE_CPP_RTTI': 'YES',
                    'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                    'MACOSX_DEPLOYMENT_TARGET': '10.8'
                }
            }], ['OS == "linux"', {
                'cflags': [],
                'cflags!': ['-fno-tree-vrp', '-fno-exceptions'],
                'cflags_cc!': ['-fno-exceptions']
            }]
        ], "dependencies": [
            "<(module_root_dir)/deps/easyloggingpp/easyloggingpp.gyp:easyloggingpp",
            "<(module_root_dir)/deps/rocksdb/rocksdb.gyp:rocksdb"
        ], "include_dirs": [
            "<!(node -e \"require('napi-macros')\")",
            "<(module_root_dir)/deps/emscripten/system/include",
        ], "sources": [
            "binding.cc"
        ]
    }]
}
