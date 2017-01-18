from types import MethodType

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'cpp' in env['TOOLS'][:-1]:
        env.Tool('system')

        def BuildCpp(env, target, sources):
            # Code to build "target" from "source"
            targets = env.Install(os.path.join(env['PREFIX'], "include", target), [source for source in sources if source.suffix in ['.h', '.hpp', '.hxx', '.h++']])
            targets += env.SharedLibrary(os.path.join(env['PREFIX'], "lib", target), [source for source in sources if source.suffix in ['.c', '.cpp', '.cxx', '.c++']])
            return targets

        env.BuildCpp = MethodType(BuildCpp, env)

def exists(env):
    return 1