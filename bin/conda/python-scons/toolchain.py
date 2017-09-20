import os
from distutils.version import LooseVersion
import subprocess
from distutils.msvccompiler import get_build_version
from sys import maxsize
from SCons.Script import AddOption, GetOption
import six

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
        SYSTEM = env['SYSTEM']
        env['ARCH'] = GetOption('arch')
        ARCH = env['ARCH']
        AddOption('--debug-symbols',
              dest    = 'debug-symbols',
              type    = 'choice',
              nargs   = 1,
              action  = 'store',
              help    = 'Debug symbols',
              default = 'no',
              choices = ['no', 'yes'])
        env['DEBUG_SYMBOLS'] = GetOption('debug-symbols')
        DEBUG_SYMBOLS = env['DEBUG_SYMBOLS']
        if DEBUG_SYMBOLS == 'yes':
            if SYSTEM == 'win':
                env.AppendUnique(CCFLAGS=['/DEBUG:FULL'])
            else:
                env.AppendUnique(CCFLAGS=['-g'])
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
        else:
            AddOption('--visbility',
                dest = 'visibility',
                type = 'choice',
                nargs = 1,
                action = 'store',
                help = 'Symbol visibility',
                choices = ['hidden', 'default'],
                default = 'hidden')
            env['VISIBILITY'] = GetOption('visibility')
            if SYSTEM == 'linux':
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
            VISIBILITY = env['VISIBILITY']
            env.PrependUnique(CPPPATH=['$PREFIX/include'],
                              LIBPATH=['$PREFIX/lib'],
                              CFLAGS=["-x", "c", "-std=c11"],
                              CCFLAGS=['-fvisibility=' + VISIBILITY],
                              CXXFLAGS=["-x", "c++", "-std=c++11"])
            if ARCH == '32':
              env.AppendUnique(CCFLAGS=['-m32'])
            if SYSTEM == 'osx':
              env.AppendUnique(CCFLAGS=['-ferror-limit=0'],
                               CXXFLAGS=['-stdlib=libc++'])
            else:
              GCC_VERSION = subprocess.check_output(['gcc','-dumpversion']).strip()
              if six.PY3:
                GCC_VERSION = GCC_VERSION.decode('ascii', 'ignore')
              diagnostics_color = LooseVersion(GCC_VERSION) >= LooseVersion('4.9') and not bool(int(os.environ.get('CONDA_BUILD', '0')))
              DIAGNOSTICS_COLOR = env['DIAGNOSTICS_COLOR']
              env.AppendUnique(CCFLAGS=['-fmax-errors=0',
                                        '-Wl,--no-undefined'] + ['-fdiagnostics-color=' + DIAGNOSTICS_COLOR] * diagnostics_color)

def exists(env):
    return 1