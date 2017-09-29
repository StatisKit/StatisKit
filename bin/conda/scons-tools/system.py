import platform
from SCons.Script import AddOption, GetOption
    
def generate(env, **kwargs):
  if not 'system' in env['TOOLS'][:-1]:
    SYSTEMS = dict(Linux   = "linux",
                   Darwin  = "osx",
                   Windows = "win")
    system = str(platform.system())
    if not system in SYSTEMS:
        raise ValueError('`' + system + '` is not a valid operating system')
    else:
      system = SYSTEMS[system]
    AddOption('--system',
                  dest    = 'system',
                  type    = 'choice',
                  nargs   = 1,
                  action  = 'store',
                  help    = 'system',
                  choices = list(SYSTEMS.values()),
                  default = system)
    env['SYSTEM'] = GetOption('system')

def exists(env):
    return 1