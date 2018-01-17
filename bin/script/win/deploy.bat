echo ON

rmdir %CONDA_PREFIX%\conda-bld\src_cache
rmdir %CONDA_PREFIX%\conda-bld\broken
for /R %%i in ("%CONDA_PREFIX%\conda-bld\*.tar.bz2") do (
    anaconda upload %%i -u %ANACONDA_UPLOAD% --label win-release
    if errorlevel 1 exit 1
)

echo OFF
