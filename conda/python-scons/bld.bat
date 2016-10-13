echo ON

if "%PY3K%" == "1" (
  2to3 --output-dir=engine/SCons3 -W -n engine/SCons
  rmdir engine/SCons /s /q
  move engine/SCons3 engine/SCons
  powershell -Command "Get-Content ".\setup.py" | select -First 49"
  powershell -Command "Get-Content ".\setup.py" | select -First 49" > setup.back
  more setup.back
)

"%PYTHON%" setup.py install --standard-lib
if errorlevel 1 exit 1
