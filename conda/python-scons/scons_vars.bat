rem set BLABLA="ABC"
rem for /f "delims=" %i in ('python -c "import os; print os.environ.get('CONDA_PREFIX').replace('/', '\\')"') do set TEMP_PREFIX=%i
rem echo %TEMP_PREFIX%
set SCONSFLAGS="--site-dir=%CONDA_PREFIX%\share\site_scons"
echo %SCONSFLAGS%