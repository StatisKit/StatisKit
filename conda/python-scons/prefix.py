import sys
from SCons.Script import AddOption, GetOption
    
added = False

def generate(env, **kwargs):
	global added
	if not added:
		added = True
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