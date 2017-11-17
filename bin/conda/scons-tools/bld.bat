:: Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ::
::                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ::
:: Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ::
::                                                                       ::
:: This file is part of the AutoWIG project. More information can be     ::
:: found at                                                              ::
::                                                                       ::
::     http://autowig.rtfd.io                                            ::
::                                                                       ::
:: The Apache Software Foundation (ASF) licenses this file to you under  ::
:: the Apache License, Version 2.0 (the "License"); you may not use this ::
:: file except in compliance with the License. You should have received  ::
:: a copy of the Apache License, Version 2.0 along with this file; see   ::
:: the file LICENSE. If not, you may obtain a copy of the License at     ::
::                                                                       ::
::     http://www.apache.org/licenses/LICENSE-2.0                        ::
::                                                                       ::
:: Unless required by applicable law or agreed to in writing, software   ::
:: distributed under the License is distributed on an "AS IS" BASIS,     ::
:: WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or       ::
:: mplied. See the License for the specific language governing           ::
:: permissions and limitations under the License.                        ::

echo ON

if not exist %PREFIX%\etc\conda\activate.d mkdir %PREFIX%\etc\conda\activate.d
copy %RECIPE_DIR%\activate.bat %PREFIX%\etc\conda\activate.d\scons_tools_vars.bat

if not exist %PREFIX%\etc\conda\activate.d mkdir %PREFIX%\etc\conda\deactivate.d
copy %RECIPE_DIR%\deactivate.bat %PREFIX%\etc\conda\deactivate.d\scons_tools_vars.bat

set TGT_DIR=scons_tools
mkdir %SP_DIR%\%TGT_DIR%
type NUL > %SP_DIR%\%TGT_DIR%\__init__.py
type NUL > %SP_DIR%\%TGT_DIR%\site_init.py
set TGT_DIR=%TGT_DIR%\site_tools
mkdir %SP_DIR%\%TGT_DIR%
type NUL > %SP_DIR%\%TGT_DIR%\__init__.py

for /r %%i in (*.py) do (
    if "%PY3K%" == "1" (
        2to3 -n -w %%i
    )
    copy %%i %SP_DIR%\%TGT_DIR%\%%~ni%%~xi
)

mkdir %SP_DIR%\scons_tools\site_autowig
if errorlevel 1 exit 1
type NUL > %SP_DIR%\scons_tools\site_autowig\__init__.py
if errorlevel 1 exit 1
mkdir %SP_DIR%\scons_tools\site_autowig\ASG
if errorlevel 1 exit 1
mkdir %SP_DIR%\scons_tools\site_autowig\parser
if errorlevel 1 exit 1
type NUL > %SP_DIR%\scons_tools\site_autowig\parser\__init__.py
if errorlevel 1 exit 1
mkdir %SP_DIR%\scons_tools\site_autowig\controller
if errorlevel 1 exit 1
type NUL > %SP_DIR%\scons_tools\site_autowig\controller\__init__.py
if errorlevel 1 exit 1
mkdir %SP_DIR%\scons_tools\site_autowig\generator
if errorlevel 1 exit 1
type NUL > %SP_DIR%\scons_tools\site_autowig\generator\__init__.py
if errorlevel 1 exit 1

echo OFF