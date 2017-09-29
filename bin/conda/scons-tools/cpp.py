import os
from SCons.Defaults import Move, Delete

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

def exists(env):
    return 1
