import sysconfig
import platform
from SCons.Script import AddOption, GetOption

AddOption('--python-version',
          dest    = 'python-version',
          type    = 'string',
          nargs   = 1,
          action  = 'store',
          help    = 'python version',
          default = sysconfig.get_python_version())
    
def generate(env, **kwargs):
    env['PYTHON_VERSION'] = GetOption('python-version')
    PYTHON_VERSION = env['PYTHON_VERSION']
    system = platform.system().lower()
    if PYTHON_VERSION is '2.7':
        if system is 'windows':
            env.Append(LIBS = 'python' + PYTHON_VERSION.replace('.', ''))
        else:
            env.Append(CPPPATH = '$PREFIX/include/python' + PYTHON_VERSION,
                       LIBS = 'python' + PYTHON_VERSION)
    else:
        raise NotImplementedError('Python ' + PYTHON_VERSION)

def exists(env):
    return 1
