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

import sysconfig
from SCons.Script import AddOption, GetOption
try:
    from path import Path
except:
    from path import path as Path
import os

def exists(env):
    return True

def generate(env, **kwargs):
    """Add Builders and construction variables to the Environment."""

    if not 'python' in env['TOOLS'][:-1]:

      env.Tool('system')
      
      PYTHON_VERSION = sysconfig.get_python_version()
      SYSTEM = env['SYSTEM']
      if SYSTEM == 'win':
          env.AppendUnique(LIBS = ['python' + PYTHON_VERSION.replace('.', '')],
                           CPPPATH = [os.path.join('$PREFIX', '..', 'include')])
      elif PYTHON_VERSION == '2.7':
              env.AppendUnique(CPPPATH = [os.path.join('$PREFIX', 'include', 'python' + PYTHON_VERSION)],
                               LIBS = ['python' + PYTHON_VERSION])
      elif PYTHON_VERSION in ['3.6', '3.7']:
              env.AppendUnique(CPPPATH = [os.path.join('$PREFIX', 'include', 'python' + PYTHON_VERSION + 'm')],
                               LIBS = ['python' + PYTHON_VERSION + 'm'])
      else:
          raise NotImplementedError('Python ' + PYTHON_VERSION)

      if SYSTEM == 'win':
        env['SP_DIR'] = os.path.join('%PREFIX%', '..', 'Lib', 'site-packages')
      else:
        env['SP_DIR'] = os.path.join('$PREFIX', 'lib', 'python' + PYTHON_VERSION, 'site-packages')
        
      def PythonPackage(env, **kwargs):
        pattern = kwargs.pop('pattern', None)
        packages = {kwarg : Path(env.Dir(kwargs[kwarg]).srcnode().abspath).walkfiles(pattern=pattern) for kwarg in kwargs}
        targets = []
        SP_DIR = env['SP_DIR']
        for package in packages:
            for source in packages[package]:
                if not source.ext in ['.lib', '.exp', '.so', '.dll']:
                    directory = os.path.join(SP_DIR, *package.split('.'))
                    directory = os.path.join(directory, source.relpath(env.Dir(kwargs[package]).srcnode().abspath).parent)
                    targets.append(env.Install(directory, source.abspath()))
        return targets

      env.AddMethod(PythonPackage)
