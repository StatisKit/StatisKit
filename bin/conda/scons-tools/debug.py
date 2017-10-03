from SCons.Script import AddOption, GetOption

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'debug' in env['TOOLS'][:-1]:
        env.Tool('system')
        env.Tool('prefix')

        AddOption('--with-nose-debug',
                  dest    = 'with-nose-debug',
                  type    = 'choice',
                  nargs   = 1,
                  action  = 'store',
                  help    = 'Degree of testing',
                  choices = ['none', 'gdb', 'pdb', 'ipdb'],
                  default = 'none')

        env['WITH_NOSE_DEBUG'] = GetOption('with-nose-debug')
        WITH_NOSE_DEBUG = env['WITH_NOSE_DEBUG']
        SYSTEM = env['SYSTEM']
        if SYSTEM == 'win':
            if WITH_NOSE_DEBUG == 'gdb':
                env.AppendUnique(CCFLAGS=['/DEBUG:FULL'])
        else:
            if WITH_NOSE_DEBUG == 'gdb':
                env.AppendUnique(CCFLAGS=['-g'])

def exists(env):
    return 1