import platform
from distutils.version import StrictVersion
from SCons.Builder import Builder
from SCons.Tool import Tool

added = False

def generate(env):
    """Add Builders and construction variables to the Environment."""
    global added
    print 'Boost.Python: ' + str(added)
    if not added:
        added = True
        from SCons.site_scons.site_tools import system
        system.generate(env)
        env.Append(LIBS = 'boost_python')
        env.AppendUnique(CPPDEFINES = ['BOOST_PYTHON_DYNAMIC_LIB',
                                       'BOOST_ALL_NO_LIB'])

        def _boost_python_module_action(target, source, env):
            # Code to build "target" from "source"
            headers = [header for header in source if header.suffix == '.h']
            sources = [source for source in source if source.suffix in ['.cpp', '.cxx', '.c++']]
            targets = list(itertools.chain(*[env.SharedObject(None, source) for source in sources]))
            SYSTEM = env['SYSTEM']
            if SYSTEM == 'linux' and len(headers) == 1:
                if len(header) == 1:
                    cmd = env.Command(header[0].target_from_source('', '.h.gch'), header, '$CXX -o $TARGET -x c++-header -c -fPIC $SHCXXFLAGS $_CCCOMCOM $SOURCE')
                    env.Depends(targets, cmd)

            source = env.File('response_file.rsp')
            with open(source.abspath, 'w') as filehandler:
                filehandler.write(' '.join(target.abspath.replace('\\','/') + ' ' for target in targets))

            env.Append(LINKFLAGS = '@' + source.abspath)

            kwargs = dict(SHLIBSUFFIX = '.so',
                          SHLIBPREFIX = '')

            if SYSTEM == 'osx':
                bpm = env.LoadableModule(target, [], LDMODULESUFFIX='.so',
                    FRAMEWORKSFLAGS = '-flat_namespace -undefined suppress', **kwargs)
            else:
                bpm = env.LoadableModule(target, [], **kwargs)

            return bpm

        env['BUILDERS']['BoostPythonModule'] = Builder(action = _boost_python_module_action)
        from SCons.site_scons.site_tools import python
        python.generate(env)
    print 'Boost.Python: ' + str(added)

def exists(env):
    return 1