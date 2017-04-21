from distutils.version import LooseVersion
import subprocess
from distutils.msvccompiler import get_build_version
from sys import maxsize
from SCons.Script import AddOption, GetOption

def generate(env):
    """Add Builders and construction variables to the Environment."""
    if not 'toolchain' in env['TOOLS'][:-1]:
      AddOption('--arch',
                dest = 'arch',
                type = 'choice',
                nargs = 1,
                action = 'store',
                help = 'Target architecture',
                choices = ['32', '64'],
                default = '64' if maxsize.bit_length() == 63 else '32')
      env.Tool('system')
      env.Tool('debug')
      SYSTEM = env['SYSTEM']
      env['ARCH'] = GetOption('arch')
      ARCH = env['ARCH']
      if SYSTEM == 'win':
        env['TARGET_ARCH'] = 'amd64' if ARCH == '64' else 'x86'
        env['HOST_ARCH'] = env['TARGET_ARCH']
        AddOption('--msvc-version',
                      dest    = 'msvc-version',
                      type    = 'string',
                      nargs   = 1,
                      action  = 'store',
                      help    = 'MSVC version',
                      default = '12.0') # str(get_build_version()))
        env['MSVC_VERSION'] = GetOption('msvc-version')
      elif SYSTEM == 'linux':
        AddOption('--diagnostics-color',
              dest    = 'diagnostics-color',
              type    = 'choice',
              nargs   = 1,
              action  = 'store',
              help    = 'Diagnostics color',
              default = 'always',
              choices=['always', 'never'])
        env['DIAGNOSTICS_COLOR'] = GetOption('diagnostics-color')
      env.Tool('default')
      env.Tool('prefix')
      if SYSTEM == 'win':
        env.AppendUnique(CCFLAGS=['/O2',
                                  '/Ob2',
                                  '/MD',
                                  '/GR',
                                  '/EHsc',
                                  '/Gy',
                                  '/GF',
                                  '/GA'],
                         CPPDEFINES=['WIN32',
                                     'UNICODE'])
        env.PrependUnique(CPPPATH=['$PREFIX\include'])
        env.PrependUnique(LIBPATH=['$PREFIX\lib',
                                   '$PREFIX\..\libs'])
      else:
        env.PrependUnique(CPPPATH=['$PREFIX/include'],
                          LIBPATH=['$PREFIX/lib'],
                          CFLAGS=["-x", "c", "-std=c11"],
                          CXXFLAGS=["-x", "c++", "-std=c++11"])
        if ARCH == '32':
          env.AppendUnique(CCFLAGS=['-m32'])
        if SYSTEM == 'osx':
          env.AppendUnique(CCFLAGS=['-ferror-limit=0'],
                           CXXFLAGS=['-stdlib=libc++'])
        else:
          diagnostics_color = LooseVersion(subprocess.check_output(['gcc','-dumpversion']).strip()) >= LooseVersion('4.9') and not bool(int(os.environ.get('CONDA_BUILD', '0')))
          DIAGNOSTICS_COLOR = env['DIAGNOSTICS_COLOR']
          env.AppendUnique(CCFLAGS=['-fmax-errors=0',
                                    '-Wl,--no-undefined',
                                    '-fvisibility=hidden'] + ['-fdiagnostics-color=' + DIAGNOSTICS_COLOR] * diagnostics_color)

def exists(env):
    return 1