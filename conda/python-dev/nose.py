from SCons.Script import AddOption, GetOption
import subprocess
import os

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'nose' in env['TOOLS'][:-1]:
      env.Tool('system')

      AddOption('--test-level',
                    dest    = 'test-level',
                    type    = 'choice',
                    nargs   = 1,
                    action  = 'store',
                    help    = 'Degree of testing',
                    choices = ['none', 'unit', 'inte', 'func'],
                    default = 'unit')
      env['TEST_LEVEL'] = GetOption('test-level')
        
      AddOption('--test-debug',
                    dest    = 'test-debug',
                    type    = 'choice',
                    nargs   = 1,
                    action  = 'store',
                    help    = 'Debuger when testing',
                    choices = ['none', 'pdb', 'ipdb'],
                    default = 'pdb')
      env['TEST_DEBUG'] = GetOption('test-debug')

      def Nosetests(env, sources, with_coverage=True, cover_tests=True, cover_inclusive=True, cover_package=''):
        noseenv = env.Clone()
        noseenv['ENV'].update(os.environ)
        TEST_LEVEL = noseenv['TEST_LEVEL']
        SYSTEM = noseenv['SYSTEM']
        categories = ['unit', 'inte', 'func']
        eval_attr = SYSTEM + "and level <= " +str(categories.index(TEST_LEVEL) + 1)
        TEST_DEBUG = noseenv['TEST_DEBUG']
        sources = [source for source in sources if source.suffix == '.py']
        if TEST_DEBUG == 'none':
            TEST_DEBUG = ''
        else:
            TEST_DEBUG = ' --' + TEST_DEBUG
        if len(sources) > 0:
            target = noseenv.Command(".coverage", sources, "nosetests $SOURCES -x -s -v"
                                                            + TEST_DEBUG
                                                            + " --with-coverage" * with_coverage
                                                            + " --cover-tests" * cover_tests
                                                            + " --cover-inclusive" * cover_inclusive
                                                            + " -A " + eval_attr
                                                            + "".join(" --cover-package=" + packagename for packagename in cover_package.split(" ") if packagename))
        return target

      env.AddMethod(Nosetests)

def exists(env):
    return 1
