import sys
import os
from SCons.Script import AddOption, GetOption
    
def generate(env, **kwargs):
  if not 'prefix' in env['TOOLS'][:-1]:
    env.Tool('system')
    SYSTEM = env['SYSTEM']
    sysprefix = sys.prefix
    if SYSTEM == 'win':
      sysprefix = os.path.join(sysprefix, 'Library')

    AddOption('--prefix',
                  dest    = 'prefix',
                  type    = 'string',
                  nargs   = 1,
                  action  = 'store',
                  metavar = 'DIR',
                  help    = 'installation prefix',
                  default = sysprefix)
    env['PREFIX'] = GetOption('prefix')

def exists(env):
    return 1