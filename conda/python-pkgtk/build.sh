set -xe

if [[ "$PY3K" = "1" ]]; then
  2to3 --output-dir=src/py3 -W -n src/py
  rm -rf src/py
  mv src/py3 src/py
  2to3 --output-dir=test3 -W -n test
  rm -rf test
  mv test3 test
fi

python setup.py install
