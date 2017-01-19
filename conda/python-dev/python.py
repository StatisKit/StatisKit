import sysconfig
from SCons.Script import AddOption, GetOption

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
              env.AppendUnique(LIBS = ['python' + PYTHON_VERSION.replace('.', '')])
          else:
              env.AppendUnique(CPPPATH = ['$PREFIX/include/python' + PYTHON_VERSION],
                               LIBS = ['python' + PYTHON_VERSION])
      else:
          raise NotImplementedError('Python ' + PYTHON_VERSION)

      if SYSTEM == 'win':
        def BuildPython(env, target, source):
            return env.Install(os.path.join(env['PREFIX'], "Lib", "site-packages"), source)
      else:
        def BuildPython(env, target, source):
            return env.Install(os.path.join(env['PREFIX'], "lib", "python" + env["PYTHON_VERSION"], 'site-packages'), source)

      env.AddMethod(BuildPython)

def exists(env):
    return 1