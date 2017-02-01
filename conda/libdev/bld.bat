echo ON

copy %RECIPE_DIR%\cpp.py %SP_DIR%\SCons\site_scons\site_tools\cpp.py
if errorlevel 1 exit 1

echo OFF
