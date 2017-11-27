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
from SCons.Defaults import Move, Delete

def exists(env):
    return True

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'cpp' in env['TOOLS'][:-1]:
        env.Tool('system')
        env.Tool('prefix')

        def CppDev(env, target, sources):
            # Code to build "target" from "source"
            SYSTEM = env['SYSTEM']
            if isinstance(target, (list, tuple)):
                return env.Install(os.path.join(env['PREFIX'], "include", *target), sources)
            else:
                return env.Install(os.path.join(env['PREFIX'], "include", target), sources)

        env.AddMethod(CppDev)

        def CppLib(env, target, sources):
            # Code to build "target" from "source"
            SYSTEM = env['SYSTEM']

            if SYSTEM == 'osx':
                kwargs = dict(FRAMEWORKSFLAGS = '-flat_namespace -undefined suppress')
            else:
                kwargs = dict()


            targets = []
            if SYSTEM == 'win':
                dll, lib, exp = env.SharedLibrary(os.path.join(env.Dir(".").abspath, target),
                                                  sources,
                                                  **kwargs)
                targets += env.Install(os.path.join(env['PREFIX'], "bin"), dll)
                targets += env.Install(os.path.join(env['PREFIX'], "lib"), lib)
            else:
                targets += env.SharedLibrary(os.path.join(env['PREFIX'], "lib", target),
                                             sources,
                                              **kwargs)
            return targets

        env.AddMethod(CppLib)