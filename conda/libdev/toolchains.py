import platform
from distutils.version import StrictVersion

def generate(env):
    """Add Builders and construction variables to the Environment."""
    system = platform.system().lower()
    if system == 'windows':
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
         env.Prepend(CPPPATH='$PREFIX\include',
                     LIBPATH='$PREFIX\lib',
                     LIBPATH='$PREFIX\..\libs')
    else:
         env.Prepend(CPPPATH='$PREFIX/include',
                     LIBPATH='$PREFIX/lib')

def exists(env):
    return 1