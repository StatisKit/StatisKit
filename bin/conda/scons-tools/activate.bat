echo ON

python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())" > temp.txt
set /p SITE_SCONS=<temp.txt
del temp.txt
sep SITE_SCONS=%SITE_SCONS%\scons_tools
if "%SCONSFLAGS%"=="" (
    set SCONSFLAGS=--site-dir=%SITE_SCONS%
) else (
    set SCONSFLAGS=%SCONSFLAGS% --site-dir=%SITE_SCONS%
)

echo OFF
