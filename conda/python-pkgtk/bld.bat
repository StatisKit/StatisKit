if "%PY3K%" == "1" 2to3 --output-dir=src/py3 -W -n src/py
if "%PY3K%" == "1" 2to3 rmdir src/py /s /q
if "%PY3K%" == "1" move src/py3 src/py
python setup.py install
