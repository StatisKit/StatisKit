echo ON

"%PYTHON%" setup.py install --standard-lib
if errorlevel 1 exit 1

if not exist %PREFIX%\etc\conda\activate.d mkdir %PREFIX%\etc\conda\activate.d
if errorlevel 1 exit 1
if not exist %PREFIX%\etc\conda\deactivate.d mkdir -p %PREFIX%\etc\conda\deactivate.d
rem type NUL > %PREFIX%\etc\conda\activate.d\scons_vars.bat
copy %RECIPE_DIR%\scons_vars.bat %PREFIX%\etc\conda\activate.d\scons_vars.bat
if errorlevel 1 exit 1
type NUL > %PREFIX%\etc\conda\deactivate.d\scons_vars.bat
if errorlevel 1 exit 1

rem echo set SCONSFLAGS="--site-dir=%CONDA_PREFIX:/=\%\share\site_scons" > %PREFIX%\etc\conda\activate.d\scons_vars.bat
if errorlevel 1 exit 1
echo set SCONSFLAGS= > %PREFIX%\etc\conda\deactivate.d\scons_vars.bat
if errorlevel 1 exit 1

if not exist %PREFIX%\share\site_scons mkdir %PREFIX%\share\site_scons
if errorlevel 1 exit 1
if not exist %PREFIX%\share\site_scons\site_init.py type NUL > %PREFIX%\share\site_scons\site_init.py
if errorlevel 1 exit 1
if not exist %PREFIX%\share\site_scons\site_tools mkdir %PREFIX%\share\site_scons\site_tools
if errorlevel 1 exit 1

copy %RECIPE_DIR%\prefix.py %PREFIX%\share\site_scons\site_tools\prefix.py
if errorlevel 1 exit 1

echo OFF
