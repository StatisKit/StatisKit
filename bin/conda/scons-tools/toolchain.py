## Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ##
##                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
## Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
##                                                                       ##
## This file is part of the StatisKit project. More information can be   ##
## found at                                                              ##
##                                                                       ##
##     http://statiskit.rtfd.io                                          ##
##                                                                       ##
## The Apache Software Foundation (ASF) licenses this file to you under  ##
## the Apache License, Version 2.0 (the "License"); you may not use this ##
## file except in compliance with the License. You should have received  ##
## a copy of the Apache License, Version 2.0 along with this file; see   ##
## the file LICENSE. If not, you may obtain a copy of the License at     ##
##                                                                       ##
##     http://www.apache.org/licenses/LICENSE-2.0                        ##
##                                                                       ##
## Unless required by applicable law or agreed to in writing, software   ##
## distributed under the License is distributed on an "AS IS" BASIS,     ##
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or       ##
## mplied. See the License for the specific language governing           ##
## permissions and limitations under the License.                        ##

import os
from distutils.version import LooseVersion
import subprocess
from sys import maxsize
from SCons.Script import AddOption, GetOption
import six

def exists(env):
    return True

def generate(env):
    """Add Builders and construction variables to the Environment."""
    if not 'toolchain' in env['TOOLS'][:-1]:
        AddOption('--arch',
                dest = 'arch',
                type = 'choice',
                nargs = 1,
                action = 'store',
                help = 'Target architecture',
                choices = ['32', '64'],
                default = '64' if maxsize.bit_length() == 63 else '32')
        env.Tool('system')
        SYSTEM = env['SYSTEM']
        env['ARCH'] = GetOption('arch')
        ARCH = env['ARCH']
        AddOption('--debug-symbols',
              dest    = 'debug-symbols',
              type    = 'choice',
              nargs   = 1,
              action  = 'store',
              help    = 'Debug symbols',
              default = 'no',
              choices = ['no', 'yes'])
        env['DEBUG_SYMBOLS'] = GetOption('debug-symbols')
        DEBUG_SYMBOLS = env['DEBUG_SYMBOLS']
        if DEBUG_SYMBOLS == 'yes':
            if SYSTEM == 'win':
                env.AppendUnique(CCFLAGS=['/DEBUG:FULL'])
            else:
                env.AppendUnique(CCFLAGS=['-g'])
        if SYSTEM == 'win':
            env['TARGET_ARCH'] = 'amd64' if ARCH == '64' else 'x86'
            env['HOST_ARCH'] = env['TARGET_ARCH']
            AddOption('--msvc-version',
                          dest    = 'msvc-version',
                          type    = 'string',
                          nargs   = 1,
                          action  = 'store',
                          help    = 'MSVC version',
                          default = '12.0')#'14.0')
            env['MSVC_VERSION'] = GetOption('msvc-version')
        else:
            AddOption('--visibility',
                dest = 'visibility',
                type = 'choice',
                nargs = 1,
                action = 'store',
                help = 'Symbol visibility',
                choices = ['hidden', 'default'],
                default = 'hidden')
            env['VISIBILITY'] = GetOption('visibility')
            if SYSTEM == 'linux':
                AddOption('--diagnostics-color',
                      dest    = 'diagnostics-color',
                      type    = 'choice',
                      nargs   = 1,
                      action  = 'store',
                      help    = 'Diagnostics color',
                      default = 'always',
                      choices=['always', 'never'])
                env['DIAGNOSTICS_COLOR'] = GetOption('diagnostics-color')
        env.Tool('default')
        env.Tool('prefix')
        if SYSTEM == 'win':
            env.AppendUnique(CCFLAGS=['/O2',
                                      '/Ob2',
                                      '/MD',
                                      '/GR',
                                      '/EHsc',
                                      '/Gy',
                                      '/GF',
                                      '/GA'],
                             CPPDEFINES=['WIN32',
                                         'UNICODE'])
            env.PrependUnique(CPPPATH=['$PREFIX\include'])
            env.PrependUnique(LIBPATH=['$PREFIX\lib',
                                       '$PREFIX\..\libs'])
        else:
            VISIBILITY = env['VISIBILITY']
            env.PrependUnique(CPPPATH=['$PREFIX/include'],
                              LIBPATH=['$PREFIX/lib'],
                              CFLAGS=["-std=c11"],
                              CCFLAGS=['-fvisibility=' + VISIBILITY],
                              CXXFLAGS=["-std=c++11"])
            # env['SHLINK'] = os.environ['LD']
            env['AR'] = os.environ['AR']
            env['AS'] = os.environ['AS']
            if ARCH == '32':
              env.AppendUnique(CCFLAGS=['-m32'])
            if SYSTEM == 'osx':
              env['CC'] = os.environ['CLANG']
              env['CXX'] = os.environ['CLANGXX']
              env.AppendUnique(
                CXXFLAGS=['-stdlib=libc++'])
            else:
              env['CC'] = os.environ['GCC']
              env['CXX'] = os.environ['GXX']
              DIAGNOSTICS_COLOR = env['DIAGNOSTICS_COLOR']
              env.AppendUnique(CCFLAGS=['-Wl,--no-undefined'] + ['-fdiagnostics-color=' + DIAGNOSTICS_COLOR])