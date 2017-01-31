echo ON

:: Set the right msvc version according to Python version
if "%PY_VER%"=="2.7" (
    set MSVC_VER=9.0
    :: set LIB_VER=90
) else if "%PY_VER%"=="3.4" (
    set MSVC_VER=10.0
    :: set LIB_VER=100
) else (
    set MSVC_VER=14.0
    :: set LIB_VER=140
)

call bootstrap.bat
if errorlevel 1 exit 1

echo Architecture: %ARCH%

CALL b2 install toolset=msvc-%MSVC_VER% ^
        address-model=%ARCH% ^
        variant=release ^
        threading=multi ^
        link=static,shared ^
        define=BOOST_ALL_NO_LIB ^
        -j%CPU_COUNT% ^
        --with-python ^
        --layout=system ^
        --build-dir=buildboost ^
        --prefix=%LIBRARY_PREFIX%
IF errorlevel 1 exit 1

:: move %LIBRARY_INC%\boost-1_61\boost %LIBRARY_INC%
:: IF errorlevel 1 exit 1

move %LIBRARY_LIB%\boost_*.dll "%LIBRARY_BIN%"
IF errorlevel 1 exit 1
