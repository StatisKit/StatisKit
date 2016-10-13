echo ON

if "%PY3K%" == "1" (
  powershell -Command "(gc engine\SCons\Errors.py) -replace 'exceptions', 'builtins --no-test' | Out-File engine\SCons\Errors.py"
  if errorlevel 1 exit 1
  powershell -Command "Get-Content "engine\SCons\Util.py" | select -First 38" > engine\SCons\Util.back
  if errorlevel 1 exit 1
  more +39 engine\SCons\Util.py >> engine\SCons\Util.back
  if errorlevel 1 exit 1
  more engine\SCons\Util.back
  if errorlevel 1 exit 1
  del engine\SCons\Util.py
  if errorlevel 1 exit 1
  move engine\SCons\Util.back engine\SCons\Util.py
  if errorlevel 1 exit 1
  2to3 --output-dir=engine\SCons3 -W -n engine\SCons
  if errorlevel 1 exit 1
  rmdir engine\SCons /s /q
  if errorlevel 1 exit 1
  move engine\SCons3 engine/SCons
  if errorlevel 1 exit 1
  powershell -Command "Get-Content ".\script\scons" | select -First 58" > script\scons.back
  if errorlevel 1 exit 1
  more +64 script\scons >> script\scons.back
  if errorlevel 1 exit 1
  del script\scons
  if errorlevel 1 exit 1
  move script\scons.back script\scons
  if errorlevel 1 exit 1
  2to3 -w -n script\scons
  if errorlevel 1 exit 1
  2to3 -w -n script\sconsign
  if errorlevel 1 exit 1
  2to3 -w -n script\scons-time
  if errorlevel 1 exit 1
  powershell -Command "Get-Content ".\setup.py" | select -First 49" > setup.back
  if errorlevel 1 exit 1
  more +54 setup.py >> setup.back
  if errorlevel 1 exit 1
  del setup.py
  if errorlevel 1 exit 1
  move setup.back setup.py
  if errorlevel 1 exit 1
)

"%PYTHON%" setup.py install --standard-lib
if errorlevel 1 exit 1
