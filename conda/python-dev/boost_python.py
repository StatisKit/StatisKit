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

            SYSTEM = env['SYSTEM']
            if not SYSTEM == 'win':
                target += '.so'
            else:
                target += '.dll'
            target = env.File(target).srcnode()
            targets = list(itertools.chain(*[env.SharedObject(None, source) for source in sources  if source.suffix in ['.cpp', '.cxx', '.c++']]))
            sources = [source for source in sources if source.suffix == '.h']
            if len(sources) == 1 and not SYSTEM == 'win':
                if SYSTEM == 'linux':
                    cmd = env.Command(sources[0].target_from_source('', '.h.gch'), sources[0], '$CXX -o $TARGET -x c++-header -c -fPIC $SHCXXFLAGS $_CCCOMCOM $SOURCE')
                else:
                    cmd = env.Command(sources[0].target_from_source('', '.h.pch'), sources[0], '$CXX -o $TARGET -x c++-header -c -fPIC $SHCXXFLAGS $_CCCOMCOM $SOURCE')
                env.Depends(targets, cmd)
                if SYSTEM == 'osx':
                    env['CXX'] += " -include " + sources[0]
            env.Depends(target, targets)
            source = env.File('response_file.rsp')
            with open(source.abspath, 'w') as filehandler:
                filehandler.write(' '.join(target.abspath.replace('\\','/') + ' ' for target in targets))
            env.Append(LINKFLAGS = '@' + source.abspath)

            if SYSTEM == 'win':
                return env.SharedLibrary(target, [])
            elif SYSTEM == 'osx':
                return env.LoadableModule(target, [],
                                          SHLINKFLAGS='$LINKFLAGS -bundle -flat_namespace -undefined suppress',
                                          SHLIBSUFFIX='.so')
            else:
                return env.LoadableModule(target, [])

        env.AddMethod(BuildBoostPython)
        env.Tool('python')

def exists(env):
    return 1