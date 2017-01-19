import platform
    
def generate(env, **kwargs):
  if not 'system' in env['TOOLS'][:-1]:
    SYSTEMS = dict(Linux   = "linux",
                   Darwin  = "osx",
                   Windows = "win")
    system = str(platform.system())
    if not system in SYSTEMS:
      system = "unknown"
    else:
      system = SYSTEMS[system]
    env.AddOption('--system',
                  dest    = 'system',
                  type    = 'choice',
                  nargs   = 1,
                  action  = 'store',
                  help    = 'system',
                  choices = SYSTEMS.values(),
                  default = system)
    env['SYSTEM'] = env.GetOption('system')
    if env['SYSTEM'] == 'unknown':
    	raise ValueError('Unknown system')

def exists(env):
    return 1