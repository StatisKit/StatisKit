echo ON

if "%PY3K%" == "1" (
  2to3 --output-dir=engine/SCons3 -W -n engine/SCons
  rmdir engine/SCons /s /q
  move engine/SCons3 engine/SCons
  2to3 -w -n scripts/scons
  2to3 -w -n scripts/sconsign
  2to3 -w -n scripts/scons-time
  powershell -Command "Get-Content ".\setup.py" | select -First 49"
  powershell -Command "Get-Content ".\setup.py" | select -First 49" > setup.back
  more +54 setup.py > setup.back
  more setup.back
  del setup.py
  move setup.back setup.py
)

"%PYTHON%" setup.py install --standard-lib
if errorlevel 1 exit 1
