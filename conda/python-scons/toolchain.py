from distutils.version import StrictVersion

def generate(env):
    """Add Builders and construction variables to the Environment."""
    if not 'toolchains' in env['TOOLS'][:-1]:
      env.Tool('default')
      env.Tool('system')
      env.Tool('prefix')
      SYSTEM = env['SYSTEM']
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
        env.PrependUnique(CPPPATH=['$PREFIX\include'])
        env.PrependUnique(LIBPATH=['$PREFIX\lib',
                                   '$PREFIX\..\libs'])
      else:
        env.PrependUnique(CPPPATH=['$PREFIX/include'],
                          LIBPATH=['$PREFIX/lib'])
        env.AppendUnique(CCFLAGS=['-ferror-limit=0'])

def exists(env):
    return 1