from distutils.version import StrictVersion
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
      SYSTEM = env['SYSTEM']
      env['ARCH'] = GetOption('arch')
      ARCH = env['ARCH']
      if SYSTEM == 'windows':
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
        if StrictVersion('8.0') <= StrictVersion(env['MSVC_VERSION']) < StrictVersion('10.0'):
            env['LINKCOM'].append('mt.exe -nologo -manifest ${TARGET}.manifest -outputresource:$TARGET;1')
            env['SHLINKCOM'].append('mt.exe -nologo -manifest ${TARGET}.manifest -outputresource:$TARGET;2')
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
        #env.AppendUnique(CXXFLAGS=['/std:c++11'])
        env.PrependUnique(CPPPATH=['$PREFIX\include'])
        env.PrependUnique(LIBPATH=['$PREFIX\lib',
                                   '$PREFIX\..\libs'])
      else:
        env.PrependUnique(CPPPATH=['$PREFIX/include'],
                          LIBPATH=['$PREFIX/lib'],
                          CFLAGS=["-x", "c++", "-std=c11"],
                          CXXFLAGS=["-x", "c++", "-std=c++11"])
        if ARCH == '32':
          env.AppendUnique(CCFLAGS=['-m32'])
        if SYSTEM == 'osx':
          env.AppendUnique(CCFLAGS=['-ferror-limit=0'],
                           CXXFLAGS=['-stdlib=libc++'])
        else:
          env.AppendUnique(CCFLAGS=['-fmax-errors=0',
                                    '-Wl,--no-undefined',
                                    '-fvisibility=hidden'])

def exists(env):
    return 1
