:: Start with bootstrap
cd .\tools\build
ECHO .\bootstrap.bat
CALL .\bootstrap.bat
:: IF errorlevel 1 exit 1
ECHO .\bootstrap.bat mingw
CALL .\bootstrap.bat mingw
