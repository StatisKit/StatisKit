import os

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'cpp' in env['TOOLS'][:-1]:
        env.Tool('system')
        env.Tool('prefix')

        def BuildCpp(env, target, sources):
            # Code to build "target" from "source"
            SYSTEM = env['SYSTEM']
            targets = env.Install(os.path.join(env['PREFIX'], "include", target),
                                  [source for source in sources if source.suffix in ['.h', '.hpp', '.hxx', '.h++']])
            if SYSTEM == 'osx':
                kwargs = dict(SHLINKFLAGS='$LINKFLAGS -dynamic',
                              SHLIBSUFFIX='.dylib')
            else:
                kwargs = dict()
            targets += env.SharedLibrary(os.path.join(env['PREFIX'], "lib", target),
                                         [source for source in sources if source.suffix in ['.c', '.cpp', '.cxx', '.c++']],
                                         **kwargs)
            return targets

        env.AddMethod(BuildCpp)

def exists(env):
    return 1