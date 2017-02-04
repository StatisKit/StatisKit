import sysconfig
from SCons.Script import AddOption, GetOption
from path import path
import os

def generate(env, **kwargs):
    """Add Builders and construction variables to the Environment."""

    if not 'python' in env['TOOLS'][:-1]:
      env.Tool('system')
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
              env.AppendUnique(LIBS = ['python' + PYTHON_VERSION.replace('.', '')],
                               CPPPATH = ['$PREFIX\..\include'])
          else:
              env.AppendUnique(CPPPATH = ['$PREFIX/include/python' + PYTHON_VERSION],
                               LIBS = ['python' + PYTHON_VERSION])
      else:
          raise NotImplementedError('Python ' + PYTHON_VERSION)

      if SYSTEM == 'win':
        env['SP_DIR'] = '$PREFIX\..\Lib\site-packages'
      else:
        env['SP_DIR'] = '$PREFIX/lib/python$PYTHON_VERSION/site-packages'
        
      def PythonPackage(env, source, pattern=None):
        source = path(env.Dir(source).srcnode().abspath)
        sources = source.walkfiles(pattern=pattern)
        targets = []
        SP_DIR = env['SP_DIR']
        for src in sources:
            if not src.ext in ['.lib', '.exp', '.so', '.dll']:
                targets.append(env.Install(os.path.join(SP_DIR, src.relpath(env.Dir('.').srcnode().abspath).parent), src.abspath()))
        return targets

      env.AddMethod(PythonPackage)

def exists(env):
    return 1
