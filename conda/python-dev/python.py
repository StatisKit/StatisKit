import sysconfig
import platform
from SCons.Script import AddOption, GetOption
from SCons.Builder import Builder
from SCons.Tool import Tool

added = False

def generate(env, **kwargs):
    global added
    print 'Python: ' + str(added)
    if not added:
      added = True
      from SCons.site_scons.site_tools import system
      system.generate(env)
      AddOption('--python-version',
                dest    = 'python-version',
                type    = 'string',
                nargs   = 1,
                action  = 'store',
                help    = 'python version',
                default = sysconfig.get_python_version())
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
      env['BUILDERS']['SetuptoolsInstallEgg'] = Builder(action = 'python $SOURCES install')
    print 'Python: ' + str(added)

def exists(env):
    return 1