## Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ##
##                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
## Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
##                                                                       ##
## This file is part of the AutoWIG project. More information can be     ##
## found at                                                              ##
##                                                                       ##
##     http://autowig.rtfd.io                                            ##
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

import platform
from SCons.Script import AddOption, GetOption
    
def exists(env):
    return True

def generate(env, **kwargs):
  if not 'system' in env['TOOLS'][:-1]:
    SYSTEMS = dict(Linux   = "linux",
                   Darwin  = "osx",
                   Windows = "win")
    system = str(platform.system())
    if not system in SYSTEMS:
        raise ValueError('`' + system + '` is not a valid operating system')
    else:
      system = SYSTEMS[system]
    AddOption('--system',
                  dest    = 'system',
                  type    = 'choice',
                  nargs   = 1,
                  action  = 'store',
                  help    = 'system',
                  choices = list(SYSTEMS.values()),
                  default = system)
    env['SYSTEM'] = GetOption('system')