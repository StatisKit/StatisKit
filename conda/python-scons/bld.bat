echo ON

if "%PY3K%" == "1" (
  powershell -Command "Get-Content ".\engine\SCons\Util.py" | select -First 38" > \engine\SCons\Util.back
  more +40 \engine\SCons\Util.py >> \engine\SCons\Util.back
  del \engine\SCons\Util.py
  move \engine\SCons\Util.back \engine\SCons\Util.py
  2to3 --output-dir=engine\SCons3 -W -n engine\SCons
  rmdir engine\SCons /s /q
  move engine\SCons3 engine/SCons
  powershell -Command "Get-Content ".\script\scons" | select -First 58" > script\scons.back
  more +64 script\scons >> script\scons.back
  del script\scons
  move script\scons.back script\scons
  2to3 -w -n script\scons
  2to3 -w -n script\sconsign
  2to3 -w -n script\scons-time
  powershell -Command "Get-Content ".\setup.py" | select -First 49" > setup.back
  more +54 setup.py >> setup.back
  del setup.py
  move setup.back setup.py
)

"%PYTHON%" setup.py install --standard-lib
if errorlevel 1 exit 1
