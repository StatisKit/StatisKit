:: Start with bootstrap
cd .\tools\build
ECHO .\bootstrap.bat
CALL .\bootstrap.bat
IF errorlevel 1 exit 1
ECHO .\bootstrap.bat mingw
CALL .\bootstrap.bat mingw
IF errorlevel 1 exit 1
ECHO .\b2.exe install toolset=gcc --prefix=%LIBRARY_PREFIX%
CALL .\b2.exe install toolset=gcc --prefix=%LIBRARY_PREFIX%