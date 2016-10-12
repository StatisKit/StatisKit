python bootstrap.py build\scons
if errorlevel 1 exit 1
cd build\scons
if errorlevel 1 exit 1
python setup.py install --standard-lib
if errorlevel 1 exit 1
:: "%PYTHON%" setup.py install --standard-lib
:: if errorlevel 1 exit 1
