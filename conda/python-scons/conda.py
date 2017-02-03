from distutils.version import StrictVersion
from distutils.msvccompiler import get_build_version
from sys import maxsize
from SCons.Script import AddOption, GetOption
from path import path
import subprocess

def generate(env):
    """Add Builders and construction variables to the Environment."""
    if not 'conda' in env['TOOLS'][:-1]:
      env.Tool('system')
      SYSTEM = env['SYSTEM']

      def Conda(sources=[], channels=['statiskit', 'conda-forge']):
        if len(sources) == 0:
            if SYSTEM == 'win':
                sources = [recipe for recipe in path(env.Dir('.').srcnode().abspath).walkdirs() if (recipe/'meta.yaml').exists() and (recipe/'bld.bat').exists()]
            else:
                sources = [recipe for recipe in path(env.Dir('.').srcnode().abspath).walkdirs() if (recipe/'meta.yaml').exists() and (recipe/'build.sh').exists()]
            for source in sources
        targets = []
      if SYSTEM == 'win':
        env['SHLIBSUFFIX'] = '.pyd'
        env['TARGET_ARCH'] = 'x86_64' if ARCH == '64' else 'x86'
        AddOption('--msvc-version',
                      dest    = 'msvc-version',
                      type    = 'string',
                      nargs   = 1,
                      action  = 'store',
                      help    = 'MSVC version',
                      default = str(get_build_version()))
        env['MSVC_VERSION'] = GetOption('msvc-version')
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
          env.AppendUnique(CCFLAGS=['-fmax-errors=0',
                                    '-Wl,--no-undefined',
                                    '-fvisibility=hidden'],
                           CPPDEFINES=['_GLIBCXX_USE_CXX11_ABI=1'])

def exists(env):
    return 1
