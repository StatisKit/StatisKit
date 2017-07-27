echo ON

pip install ipdb
pip install ipdbplugin
copy %RECIPE_DIR%\boost_python.py %SP_DIR%\SCons\site_scons\site_tools\boost_python.py
if errorlevel 1 exit 1
copy %RECIPE_DIR%\python.py %SP_DIR%\SCons\site_scons\site_tools\python.py
if errorlevel 1 exit 1
copy %RECIPE_DIR%\nose.py %SP_DIR%\SCons\site_scons\site_tools\nose.py
if errorlevel 1 exit 1

echo OFF