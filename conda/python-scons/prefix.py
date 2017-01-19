import sys
    
def generate(env, **kwargs):
  if not 'prefix' in env['TOOLS'][:-1]:
    env.AddOption('--prefix',
                  dest    = 'prefix',
                  type    = 'string',
                  nargs   = 1,
                  action  = 'store',
                  metavar = 'DIR',
                  help    = 'installation prefix',
                  default = sys.prefix)
    env['PREFIX'] = env.GetOption('prefix')

def exists(env):
    return 1