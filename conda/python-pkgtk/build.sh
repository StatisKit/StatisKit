if [[ "$PY3K" = "1" ]]; then
  2to3 --output-dir=src/py3 -W -n src/py
  rm -rf src/py
  mv src/py3 src/py
fi
python setup.py install
