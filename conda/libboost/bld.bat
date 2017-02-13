echo ON

dir
del .\bld.bat
dir 


:: Set the right msvc version according to Python version
if "%PY_VER%"=="2.7" (
    set MSVC_VER=9.0
    set LIB_VER=90
) else if "%PY_VER%"=="3.4" (
    set MSVC_VER=10.0
    set LIB_VER=100
) else (
    set MSVC_VER=14.0
    set LIB_VER=140
)

set MSVC_VER=14.0
set LIB_VER=140

call bootstrap.bat
if errorlevel 1 exit 1

call b2 install toolset=msvc-%MSVC_VER% ^
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
if errorlevel 1 exit 1

move %LIBRARY_LIB%\boost_*.dll "%LIBRARY_BIN%"
if errorlevel 1 exit 1

echo OFF
