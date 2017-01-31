import os
from SCons.Defaults import Delete

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

            if SYSTEM == 'win':
                win_targets = env.SharedLibrary(os.path.join(env['PREFIX'], "lib", target),
                                                [source for source in sources if source.suffix in ['.c', '.cpp', '.cxx', '.c++']],
                                                **kwargs)
                targets += env.Install(os.path.join(env['PREFIX'], "bin"),
                                       [target for target in win_targets if target.suffix == '.dll'])
                targets += [target for target in win_targets if target.suffix == '.lib']
                Delete([target for target in win_targets if not target.suffix == '.lib'])
            else:
                targets += env.SharedLibrary(os.path.join(env['PREFIX'], "lib", target),
                                             [source for source in sources if source.suffix in ['.c', '.cpp', '.cxx', '.c++']],
                                             **kwargs)
            return targets

        env.AddMethod(BuildCpp)

def exists(env):
    return 1
