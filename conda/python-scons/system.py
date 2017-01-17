import platform
from SCons.Script import AddOption, GetOption

added = False
    
def generate(env, **kwargs):
  global added
  if not added:
    added = True
    SYSTEMS = dict(Linux   = "linux",
             Darwin  = "osx",
             Windows = "win")
    system = str(platform.system())
    if not system in SYSTEMS:
      system = "unknown"
    AddOption('--system',
              dest    = 'system',
              type    = 'choice',
              nargs   = 1,
              action  = 'store',
              help    = 'system',
              choices = SYSTEMS.values(),
              default = system)
    env['SYSTEM'] = GetOption('system')
    if env['SYSTEM'] == 'unknown':
    	raise ValueError('Unknown system')

def exists(env):
    return 1