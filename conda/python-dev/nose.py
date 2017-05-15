from SCons.Script import AddOption, GetOption
import subprocess
import os

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
                    FLAGS += ' --' + WITH_NOSE_DEBUG + '-failures'
                if len(sources) > 0:
                    target = noseenv.Command(".coverage", sources, "nosetests $SOURCES" + FLAGS)
                    return target

        env.AddMethod(Nosetests)

def exists(env):
    return 1
