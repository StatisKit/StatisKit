import sys
from SCons.Script import AddOption, GetOption

def generate(env, **kwargs):
    env['PREFIX'] = GetOption('prefix')

def exists(env):
    AddOption('--prefix',
              dest    = 'prefix',
              type    = 'string',
              nargs   = 1,
              action  = 'store',
              metavar = 'DIR',
              help    = 'installation prefix',
              default = sys.prefix)
    return 1
