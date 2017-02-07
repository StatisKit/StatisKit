echo ON

copy %RECIPE_DIR%\nose.py %SP_DIR%\SCons\site_scons\site_tools\nose.py
if errorlevel 1 exit 1

echo OFF