ECHO b2 install toolset=gcc ^
        address-model=%ARCH% ^
        variant=release ^
        threading=multi ^
        link=shared ^
        -j%CPU_COUNT% ^
        --with-python ^
        --build-dir=buildboost ^
        --prefix=%LIBRARY_PREFIX%
CALL b2 install toolset=gcc ^
        address-model=%ARCH% ^
        variant=release ^
        threading=multi ^
        link=shared ^
        -j%CPU_COUNT% ^
        --with-python ^
        --build-dir=buildboost ^
        --prefix=%LIBRARY_PREFIX%
IF errorlevel 1 exit 1

ECHO move %LIBRARY_INC%\boost-1_61\boost %LIBRARY_INC%
move %LIBRARY_INC%\boost-1_61\boost %LIBRARY_INC%
IF errorlevel 1 exit 1

ECHO %LIBRARY_LIB%\*mingw49-mt-1_61.dll "%LIBRARY_BIN%"
move %LIBRARY_LIB%\*mingw49-mt-1_61.dll "%LIBRARY_BIN%"
IF errorlevel 1 exit 1