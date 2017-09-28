import sysconfig
from SCons.Script import AddOption, GetOption
try:
    from path import Path
except:
    from path import path as Path
import os

def generate(env, **kwargs):
    """Add Builders and construction variables to the Environment."""

    if not 'python' in env['TOOLS'][:-1]:

      env.Tool('system')
      
      PYTHON_VERSION = sysconfig.get_python_version()
      SYSTEM = env['SYSTEM']
      if SYSTEM == 'win':
          env.AppendUnique(LIBS = ['python' + PYTHON_VERSION.replace('.', '')],
                           CPPPATH = ['$PREFIX\..\include'])
      elif PYTHON_VERSION == '2.7':
              env.AppendUnique(CPPPATH = ['$PREFIX/include/python' + PYTHON_VERSION],
                               LIBS = ['python' + PYTHON_VERSION])
      elif PYTHON_VERSION == '3.6':
              env.AppendUnique(CPPPATH = ['$PREFIX/include/python' + PYTHON_VERSION + 'm'],
                               LIBS = ['python' + PYTHON_VERSION + 'm'])
      else:
          raise NotImplementedError('Python ' + PYTHON_VERSION)

      if SYSTEM == 'win':
        env['SP_DIR'] = '$PREFIX\..\Lib\site-packages'
      else:
        env['SP_DIR'] = '$PREFIX/lib/python' + PYTHON_VERSION + '/site-packages'
        
      def PythonPackage(env, **kwargs):
        pattern = kwargs.pop('pattern', None)
        packages = {kwarg : Path(env.Dir(kwargs[kwarg]).srcnode().abspath).walkfiles(pattern=pattern) for kwarg in kwargs}
        targets = []
        SP_DIR = env['SP_DIR']
        for package in packages:
            for source in packages[package]:
                if not source.ext in ['.lib', '.exp', '.so', '.dll']:
                    directory = os.path.join(SP_DIR, *package.split('.'))
                    directory = os.path.join(directory, source.relpath(env.Dir(kwargs[package]).srcnode().abspath).parent)
                    targets.append(env.Install(directory, source.abspath()))
        return targets

      env.AddMethod(PythonPackage)

def exists(env):
    return 1
