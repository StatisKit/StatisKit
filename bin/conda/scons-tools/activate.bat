python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())" > temp.txt
set /p STK_SP_DIR=<temp.txt
del temp.txt
set SCONSFLAGS=%SCONSFLAGS% --site-dir=%STK_SP_DIR%\scons-tools