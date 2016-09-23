:: Start with bootstrap
CALL bootstrap.bat mingw
IF errorlevel 1 exit 1

:: Build step
CALL b2 install ^
    --build-dir=buildboost ^
    --prefix=%LIBRARY_PREFIX% ^
    toolset=gcc ^
    address-model=%ARCH% ^
    variant=release ^
    threading=multi ^
    link=shared ^
    -j%CPU_COUNT% ^
    -s ZLIB_INCLUDE="%LIBRARY_INC%" ^
    -s ZLIB_LIBPATH="%LIBRARY_LIB%" ^
    --with-python
IF errorlevel 1 exit 1

:: Install fix-up for a non version-specific boost include
move %LIBRARY_INC%\boost-1_61\boost %LIBRARY_INC%
IF errorlevel 1 exit 1

:: Move dll's to LIBRARY_BIN
move %LIBRARY_LIB%\*vc%LIB_VER%-mt-1_61.dll "%LIBRARY_BIN%"
IF errorlevel 1 exit 1
Status API Training Shop Blog About
