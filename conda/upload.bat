echo OFF

set UPLOAD_TARGETS=python-parse python-pkgtk

if "%ANACONDA_USERNAME%" == "" (
  set /p ANACONDA_USERNAME="Username: "
) else (
  echo Username: %ANACONDA_USERNAME%;
)

if "%ANACONDA_PASSWORD%" == "" (
  set /p ANACONDA_USERNAME=%ANACONDA_USERNAME%%"'s password: "
) else (
  echo %ANACONDA_USERNAME%'s password: [secure];
)

set ANACONDA_UPLOAD_FLAGS=-c conda-forge %ANACONDA_UPLOAD_FLAGS%
if "%ANACONDA_CHANNEL%" == "" (
    set ANACONDA_CHANNEL=statiskit
) else (
    echo Using anaconda channel: %ANACONDA_CHANNEL%
    set ANACONDA_UPLOAD_FLAGS=-c statiskit %ANACONDA_UPLOAD_FLAGS%
)

echo ON

conda install -n root anaconda-client
if %errorlevel% neq 0 (
  exit /b %errorlevel%
)

echo OFF

echo y|anaconda login --username %ANACONDA_USERNAME% --password %ANACONDA_PASSWORD%
if %errorlevel% neq 0 (
  exit /b %errorlevel%
)

echo ON

git clone https://gist.github.com/c491cb08d570beeba2c417826a50a9c3.git toolchain
if %errorlevel% neq 0 (
  anaconda logout
  exit /b %errorlevel%
)
cd toolchain
call config.bat
if %errorlevel% neq 0 (
  cd ..
  anaconda logout
  rmdir toolchain /s /q
  exit /b %errorlevel%
)
cd ..
rmdir toolchain /s /q

for %%x in (%UPLOAD_TARGETS%) do (
  <nul set /p="for /f %%%%i in ('conda build " >> _upload.bat
  <nul set /p=%%x >> _upload.bat
  <nul set /p=" -c " >> _upload.bat
  <nul set /p=%ANACONDA_CHANNEL% >> _upload.bat
  <nul set /p=" " >> _upload.bat
  <nul set /p=%ANACONDA_UPLOAD_FLAGS% >> _upload.bat
  <nul set /p=" --output') do set UPLOAD_FILE=%%%%i" >> _upload.bat
  echo. >> _upload.bat
  <nul set /p="anaconda upload --user " >> _upload.bat
  <nul set /p=%ANACONDA_CHANNEL% >> _upload.bat
  <nul set /p=" %%UPLOAD_FILE%%" >> _upload.bat
  echo. >> _upload.bat
  <nul set /p="if %%errorlevel%% neq 0 " >> _upload.bat
  echo echo upload failed >> _upload
  call _upload.bat
  del _upload.bat
)

anaconda logout
