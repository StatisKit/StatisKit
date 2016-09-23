:: Start with bootstrap
cd .\tools\build
ECHO .\bootstrap.bat
CALL .\bootstrap.bat
IF errorlevel 1 exit 1
ECHO .\bootstrap.bat mingw
CALL .\bootstrap.bat mingw
IF errorlevel 1 exit 1
ECHO .\b2.exe install toolset=gcc --prefix=%SRC_DIR%\b2_for_mingw
CALL .\b2.exe install toolset=gcc --prefix=%SRC_DIR%\b2_for_mingw
ECHO cd %SRCDIR%
cd %SRCDIR%
set PATH=%PATH%;%SRCDIR%\b2_for_mingw\bin
ECHO b2 toolset=gcc --build-type=complete stage ^
     --build-dir=buildboost ^
     --prefix=%LIBRARY_PREFIX% ^
     address-model=%ARCH% ^
     variant=release ^
     threading=multi ^
     link=shared ^
     -j%CPU_COUNT% ^
     -s ZLIB_INCLUDE="%LIBRARY_INC%" ^
     -s ZLIB_LIBPATH="%LIBRARY_LIB%" ^
     --with-python
CALL b2 toolset=gcc --build-type=complete stage ^
     --build-dir=buildboost ^
     --prefix=%LIBRARY_PREFIX% ^
     address-model=%ARCH% ^
     variant=release ^
     threading=multi ^
     link=shared ^
     -j%CPU_COUNT% ^
     -s ZLIB_INCLUDE="%LIBRARY_INC%" ^
     -s ZLIB_LIBPATH="%LIBRARY_LIB%" ^
     --with-python
     
:: cd ..\..
:: dir .
:: CALL .\tools\build\b2.exe install toolset=gcc --prefix=%LIBRARY_PREFIX%
:: dir .
:: set PATH=%PATH%;%LIBRARY_BIN%
:: 
:: Build step
:: CALL b2 install ^
::     --build-dir=buildboost ^
::     --prefix=%LIBRARY_PREFIX% ^
::     toolset=gcc ^
::     address-model=%ARCH% ^
::     variant=release ^
::     threading=multi ^
::     link=shared ^
::     -j%CPU_COUNT% ^
::     -s ZLIB_INCLUDE="%LIBRARY_INC%" ^
::     -s ZLIB_LIBPATH="%LIBRARY_LIB%" ^
::     --with-python
:: IF errorlevel 1 exit 1
:: 
:: :: Install fix-up for a non version-specific boost include
:: move %LIBRARY_INC%\boost-1_61\boost %LIBRARY_INC%
:: IF errorlevel 1 exit 1
:: 
:: Move dll's to LIBRARY_BIN
:: move %LIBRARY_LIB%\*vc%LIB_VER%-mt-1_61.dll "%LIBRARY_BIN%"
:: IF errorlevel 1 exit 1
:: Status API Training Shop Blog About
