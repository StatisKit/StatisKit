echo ON

python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())" > temp.txt
set /p TMP_DIR=<temp.txt
del temp.txt
set SCONSFLAGS=%SCONSFLAGS% --site-dir=%TMP_DIR%\scons-tools
set TMP_DIR=

echo OFF