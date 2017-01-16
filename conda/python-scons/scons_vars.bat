set BLABLA="ABC"
for /f "delims=" %i in ('python -c "import os; print os.environ.get('CONDA_PREFIX').replace('/', '\\')"') do set TEMP_PREFIX=%i
echo %TEMP_PREFIX%
set SCONSFLAGS="--site-dir=%TEMP_PREFIX%/share/site_scons"
echo %SCONSFLAGS%