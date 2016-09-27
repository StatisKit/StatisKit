:: Start with bootstrap
:: cd .\tools\build
ECHO .\bootstrap.bat
CALL .\bootstrap.bat
IF errorlevel 1 exit 1
ECHO .\bootstrap.bat gcc
CALL .\bootstrap.bat gcc
IF errorlevel 1 exit 1
ECHO .\b2.exe install toolset=gcc --prefix=%SRC_DIR%\b2_for_mingw
CALL .\b2.exe install toolset=gcc --prefix=%SRC_DIR%\b2_for_mingw
IF errorlevel 1 exit 1
ECHO cd %SRC_DIR%
cd %SRC_DIR%
IF errorlevel 1 exit 1
set PATH=%PATH%;%SRC_DIR%\b2_for_mingw\bin
IF errorlevel 1 exit 1
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
CALL b2 toolset=gcc ^
        address-model=%ARCH% ^
        variant=release ^
        threading=multi ^
        link=shared ^
        -j%CPU_COUNT% ^
        -s ZLIB_INCLUDE="%LIBRARY_INC%" ^
        -s ZLIB_LIBPATH="%LIBRARY_LIB%" ^
        --with-python ^
        --build-dir=buildboost ^
        --prefix=%LIBRARY_PREFIX%
IF errorlevel 1 exit 1
move %LIBRARY_INC%\boost-1_61\boost %LIBRARY_INC%
IF errorlevel 1 exit 1

move %LIBRARY_LIB%\*vc%LIB_VER%-mt-1_61.dll "%LIBRARY_BIN%"
IF errorlevel 1 exit 1
