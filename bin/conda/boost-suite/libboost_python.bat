echo ON

python %RECIPE_DIR%\\move.py --src=%SRC_DIR%\\Library\\lib --dst=%PREFIX%\\Library\\lib --include=boost_python
python %RECIPE_DIR%\\move.py --src=%SRC_DIR%\\Library\\bin --dst=%PREFIX%\\Library\\bin --include=boost_python

echo OFF