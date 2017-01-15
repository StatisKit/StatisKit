import sys
from SCons.Script import AddOption, GetOption

AddOption('--prefix',
          dest    = 'prefix',
          type    = 'string',
          nargs   = 1,
          action  = 'store',
          metavar = 'DIR',
          help    = 'installation prefix',
          default = sys.prefix)
    
def generate(env, **kwargs):
    env['PREFIX'] = GetOption('prefix')

def exists(env):
    return 1
