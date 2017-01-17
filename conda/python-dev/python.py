import sysconfig
import platform
from SCons.Script import AddOption, GetOption
from SCons.Builder import Builder

AddOption('--python-version',
          dest    = 'python-version',
          type    = 'string',
          nargs   = 1,
          action  = 'store',
          help    = 'python version',
          default = sysconfig.get_python_version())
    
_setuptools_install_builder = Builder(action = 'python $SOURCES install')

def generate(env, **kwargs):
    env['PYTHON_VERSION'] = GetOption('python-version')
    PYTHON_VERSION = env['PYTHON_VERSION']
    SYSTEM = env['SYSTEM']
    if PYTHON_VERSION == '2.7':
        if SYSTEM == 'win':
            env.Append(LIBS = 'python' + PYTHON_VERSION.replace('.', ''))
        else:
            env.Append(CPPPATH = '$PREFIX/include/python' + PYTHON_VERSION,
                       LIBS = 'python' + PYTHON_VERSION)
    else:
        raise NotImplementedError('Python ' + PYTHON_VERSION)
    env['BUILDERS']['SetuptoolsInstallEgg'] = _setuptools_install_builder

def exists(env):
    return 1
