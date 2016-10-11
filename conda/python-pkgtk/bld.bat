if "%PY3K%" == "1" 2to3 --output-dir=src/py3 -W -n src/py
if "%PY3K%" == "1" 2to3 rmdir src/py /s /q
if "%PY3K%" == "1" move src/py3 src/py
if "%PY3K%" == "1" 2to3 --output-dir=test3 -W -n test
if "%PY3K%" == "1" 2to3 rmdir test /s /q
if "%PY3K%" == "1" move test3 test
python setup.py install
