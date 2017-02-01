import os
from SCons.Defaults import Move

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'cpp' in env['TOOLS'][:-1]:
        env.Tool('system')
        env.Tool('prefix')

        def BuildCpp(env, target, sources):
            # Code to build "target" from "source"
            SYSTEM = env['SYSTEM']
            targets = env.Install(os.path.join(env['PREFIX'], "include", *target.split('_')),
                                  [source for source in sources if source.suffix in ['.h', '.hpp', '.hxx', '.h++']])
            if SYSTEM == 'osx':
                kwargs = dict(FRAMEWORKSFLAGS = '-flat_namespace -undefined suppress')
            else:
                kwargs = dict()

            targets += env.SharedLibrary(os.path.join(env['PREFIX'], "lib", target),
                                         [source for source in sources if source.suffix in ['.c', '.cpp', '.cxx', '.c++']],
                                         **kwargs)
            if SYSTEM == 'win':
                dll = [target for target in targets if target.suffix == '.dll'].pop()
                exp = [target for target in targets if target.suffix == '.exp'].pop()
                lib = [target for target in targets if target.suffix == '.lib'].pop()
                targets = [target for target in targets if not target.suffix in ['.dll', '.exp', '.lib']]
                targets += env.Install(os.path.join(env['PREFIX'], "bin"), dll)
                targets += env.Command(lib, [exp, dll], [Delete("$SOURCE")])
            return targets

        env.AddMethod(BuildCpp)

def exists(env):
    return 1
