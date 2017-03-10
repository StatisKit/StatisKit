from SCons.Script import AddOption, GetOption
import subprocess

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'nose' in env['TOOLS'][:-1]:
      env.Tool('system')
      AddOption('--with-test',
                    dest    = 'with-test',
                    type    = 'choice',
                    nargs   = 1,
                    action  = 'store',
                    help    = 'Degree of testing',
                    choices = ['none', 'unit', 'inte', 'func'],
                    default = 'unit')

      env['WITH_TEST'] = GetOption('with-test')
        
      def Nosetests(env, sources, with_debug='pdb', with_coverage=True, cover_tests=True, cover_inclusive=True, cover_package=''):
        WITH_TEST = env['WITH_TEST']
        if WITH_TEST == 'none':
            sources = []
        elif WITH_TEST == 'unit':
            sources = [source for source in sources if source.name.startswith('test_unit_')]
        elif WITH_TEST == 'inte':
            sources = [source for source in sources if source.name.startswith('test_unit_') or source.name.startswith('test_inte_')]
        elif WITH_TEST == 'func':
            sources = [source for source in sources if source.name.startswith('test_unit_') or source.name.startswith('test_inte_') or source.name.startswith('test_func_')]
        sources = [source for source in sources if source.suffix == '.py']
        SYSTEM = env['SYSTEM']
        if SYSTEM == 'win':
            nosetests = subprocess.check_output(['where', 'nosetests']).strip()
        else:
            nosetests = subprocess.check_output(['which', 'nosetests']).strip()
        if with_debug == 'none':
            with_debug = ''
        elif with_debug == 'pdb':
            with_debug = ' --pdb'
        elif with_debug == 'ipdb':
            with_debug = ' --ipdb'
        if len(sources) > 0:
            target = env.Command(".coverage", sources, nosetests + " $SOURCES -x -s -v" + with_debug + " --with-coverage" * with_coverage + " --cover-tests" * cover_tests + " --cover-inclusive" * cover_inclusive + "".join(" --cover-package=" + packagename for packagename in cover_package.split(" ") if packagename))
            return target

      env.AddMethod(Nosetests)

def exists(env):
    return 1
