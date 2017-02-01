echo ON

git config --system alias.co checkout
if errorlevel 1 exit 1
git config --system alias.br branch
if errorlevel 1 exit 1
git config --system alias.ci commit
if errorlevel 1 exit 1
git config --system alias.st status
if errorlevel 1 exit 1
git config --system alias.unstage reset HEAD --
if errorlevel 1 exit 1
git config --system alias.last log -1 HEAD
if errorlevel 1 exit 1
git config --system credential.helper cache --timeout=3600
if errorlevel 1 exit 1

echo OFF
