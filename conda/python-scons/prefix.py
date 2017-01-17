import sys
from SCons.Script import AddOption, GetOption
    
def generate(env, **kwargs):
  if not 'prefix' in env['TOOLS']:
    AddOption('--prefix',
                  dest    = 'prefix',
                  type    = 'string',
                  nargs   = 1,
                  action  = 'store',
                  metavar = 'DIR',
                  help    = 'installation prefix',
                  default = sys.prefix)
    env['PREFIX'] = GetOption('prefix')

def exists(env):
    return 1