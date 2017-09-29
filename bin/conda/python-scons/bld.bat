echo ON

python setup.py install --standard-lib --prefix=%PREFIX%
if errorlevel 1 exit 1

copy %RECIPE_DIR%\scons.bat %PREFIX%\Scripts\scons.bat
if errorlevel 1 exit 1

echo OFF
