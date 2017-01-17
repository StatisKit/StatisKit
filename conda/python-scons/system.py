import platform
from SCons.Script import AddOption, GetOption

SYSTEMS = dict(Linux   = "linux",
	           Darwin  = "osx",
	           Windows = "windows")


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
    
def generate(env, **kwargs):
    env['SYSTEM'] = GetOption('system')
    if env['SYSTEM'] == 'unknown':
    	raise ValueError('Unknown system')

def exists(env):
    return 1