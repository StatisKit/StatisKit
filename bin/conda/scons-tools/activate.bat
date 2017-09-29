python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())" > temp.txt
set /p SP_DIR=<temp.txt
del temp.txt
set SCONSFLAGS=%SCONSFLAGS% --site-dir=%SP_DIR%\scons-tools