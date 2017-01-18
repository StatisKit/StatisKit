from types import MethodType
import itertools

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'boost_python' in env['TOOLS'][:-1]:
        env.Tool('system')
        env.AppendUnique(LIBS = ['boost_python'])
        env.AppendUnique(CPPDEFINES = ['BOOST_PYTHON_DYNAMIC_LIB',
                                       'BOOST_ALL_NO_LIB'])

        def BuildBoostPython(env, target, sources):
            # Code to build "target" from "source"
            target = env.File(target).srcnode()
            targets = list(itertools.chain(*[env.SharedObject(None, source) for source in sources  if source.suffix in ['.cpp', '.cxx', '.c++']]))
            print sources
            sources = [source for source in sources if source.suffix == '.h']
            print sources
            SYSTEM = env['SYSTEM']
            print SYSTEM
            if SYSTEM == 'linux' and len(sources) == 1:
                cmd = env.Command(sources[0].target_from_source('', '.h.gch'), sources[0], '$CXX -o $TARGET -x c++-header -c -fPIC $SHCXXFLAGS $_CCCOMCOM $SOURCE')
                env.Depends(targets, cmd)
            env.Depends(target, targets)
            source = env.File('response_file.rsp')
            with open(source.abspath, 'w') as filehandler:
                filehandler.write(' '.join(target.abspath.replace('\\','/') + ' ' for target in targets))
            env.Append(LINKFLAGS = '@' + source.abspath)

            kwargs = dict(SHLIBSUFFIX = '.so',
                          SHLIBPREFIX = '')
            if SYSTEM == 'osx':
                return env.LoadableModule(target, [], LDMODULESUFFIX='.so',
                    FRAMEWORKSFLAGS = '-flat_namespace -undefined suppress', **kwargs)
            else:
                return env.LoadableModule(target, [], **kwargs)

        env.BuildBoostPython = MethodType(BuildBoostPython, env)
        env.Tool('python')

def exists(env):
    return 1