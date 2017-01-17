echo ON

"%PYTHON%" setup.py install --standard-lib
if errorlevel 1 exit 1

if not exist %PREFIX%\etc\conda\activate.d mkdir %PREFIX%\etc\conda\activate.d
if errorlevel 1 exit 1
if not exist %PREFIX%\etc\conda\deactivate.d mkdir -p %PREFIX%\etc\conda\deactivate.d
type NUL > %PREFIX%\etc\conda\activate.d\scons_vars.bat
rem copy %RECIPE_DIR%\scons_vars.bat %PREFIX%\etc\conda\activate.d\scons_vars.bat
if errorlevel 1 exit 1
type NUL > %PREFIX%\etc\conda\deactivate.d\scons_vars.bat
if errorlevel 1 exit 1

echo set SCONSFLAGS=--site-dir=%CONDA_PREFIX:/=\%\Lib\site-packages\SCons\site_scons > %PREFIX%\etc\conda\activate.d\scons_vars.bat
if errorlevel 1 exit 1
echo set SCONSFLAGS= > %PREFIX%\etc\conda\deactivate.d\scons_vars.bat
if errorlevel 1 exit 1

if not exist %SP_DIR%\SCons\site_scons mkdir %SP_DIR%\SCons\site_scons
if errorlevel 1 exit 1
if not exist %SP_DIR%\SCons\site_scons\__init__.py type NUL > %SP_DIR%\SCons\site_scons\__init__.py
if errorlevel 1 exit 1
if not exist %SP_DIR%\SCons\site_scons\site_init.py type NUL > %SP_DIR%\SCons\site_scons\site_init.py
if errorlevel 1 exit 1
if not exist %SP_DIR%\SCons\site_scons\site_tools mkdir %SP_DIR%\SCons\site_scons\site_tools
if errorlevel 1 exit 1
if not exist %SP_DIR%\SCons\site_scons\site_tools\__init__.py type NUL > %SP_DIR%\SCons\site_scons\site_tools\__init__.py
if errorlevel 1 exit 1
copy %RECIPE_DIR%\prefix.py %SP_DIR%\SCons\site_scons\site_tools\prefix.py
if errorlevel 1 exit 1
copy %RECIPE_DIR%\system.py %SP_DIR%\SCons\site_scons\site_tools\system.py
if errorlevel 1 exit 1

echo OFF
