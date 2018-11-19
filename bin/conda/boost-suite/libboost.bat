echo ON

python %RECIPE_DIR%\\move.py --src=%SRC_DIR%\\Library\\lib --dst=%PREFIX%\\Library\\lib --exclude=boost_python
python %RECIPE_DIR%\\move.py --src=%SRC_DIR%\\Library\\bin --dst=%PREFIX%\\Library\\bin --exclude=boost_python

echo OFF