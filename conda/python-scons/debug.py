from SCons.Script import AddOption, GetOption

def generate(env):
    """Add Builders and construction variables to the Environment."""
    
    if not 'debug' in env['TOOLS'][:-1]:
        env.Tool('system')
        env.Tool('prefix')

        AddOption('--with-debug',
                  dest    = 'with-debug',
                  type    = 'choice',
                  nargs   = 1,
                  action  = 'store',
                  help    = 'Degree of testing',
                  choices = ['none', 'full'],
                  default = 'none')

        env['WITH_DEBUG'] = GetOption('with-debug')
        WITH_DEBUG = env['WITH_DEBUG']
        SYSTEM = env['SYSTEM']
        if SYSTEM == 'win':
            if WITH_DEBUG == 'full':
                env.AppendUnique(CCFLAGS=['/DEBUG:FULL'])
        else:
            if WITH_DEBUG == 'full':
                env.AppendUnique(CCFLAGS=['-g'])

def exists(env):
    return 1