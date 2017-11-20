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

from SCons.Script import AddOption, GetOption
import subprocess
import os

def exists(env):
  return True

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'nose' in env['TOOLS'][:-1]:
        env.Tool('system')
        env.Tool('python')
        env.Tool('textfile')

        AddOption('--test-level',
                  dest    = 'test-level',
                  type    = 'choice',
                  nargs   = 1,
                  action  = 'store',
                  help    = 'Degree of testing',
                  choices = ['none', 'unit', 'inte', 'func'],
                  default = 'unit')
        env['TEST_LEVEL'] = GetOption('test-level')

        AddOption('--with-nose-debug',
                  dest    = 'with-nose-debug',
                  type    = 'choice',
                  nargs   = 1,
                  action  = 'store',
                  help    = 'Degree of testing',
                  choices = ['none', 'gdb', 'pdb', 'ipdb'],
                  default = 'none')

        env['WITH_NOSE_DEBUG'] = GetOption('with-nose-debug')

        def Nosetests(env, sources, with_coverage=True, cover_tests=True, cover_inclusive=True, cover_package=''):
            noseenv = env.Clone()
            noseenv['ENV'].update(os.environ)
            TEST_LEVEL = noseenv['TEST_LEVEL']
            SYSTEM = noseenv['SYSTEM']
            SP_DIR = noseenv['SP_DIR']
            categories = ['none', 'unit', 'inte', 'func']
            FLAGS = " -s -v"
            FLAGS += ' -A "' + SYSTEM + ' and level <= ' +str(categories.index(TEST_LEVEL)) + '"'
            FLAGS += " --with-coverage --cover-erase" * with_coverage
            FLAGS += " --cover-tests" * cover_tests * with_coverage
            FLAGS += " --cover-inclusive" * cover_inclusive * with_coverage
            FLAGS += "".join(" --cover-package=" + packagename for packagename in cover_package.split(" ") if packagename) * with_coverage
            WITH_NOSE_DEBUG = noseenv['WITH_NOSE_DEBUG']
            sources = [source for source in sources if source.suffix == '.py']
            if WITH_NOSE_DEBUG == 'gdb':
                if len(sources) > 0:
                    targets = noseenv.Textfile(target = 'nosetests.gdb',
                                               source = ["run " + os.path.join(SP_DIR, "nose", "core.py") + " " + " ".join(source.abspath for source in sources) + FLAGS])
                    targets += noseenv.Command(".coverage", targets, "gdb python < $SOURCES")
                    return targets
            else:
                if not WITH_NOSE_DEBUG == 'none':
                    FLAGS += ' --' + WITH_NOSE_DEBUG + ' --' + WITH_NOSE_DEBUG + '-failures'
                if len(sources) > 0:
                    target = noseenv.Command(".coverage", sources, "nosetests $SOURCES" + FLAGS)
                    return target

        env.AddMethod(Nosetests)
