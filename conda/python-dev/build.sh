set -ve

cp $RECIPE_DIR/boost_python.py $SP_DIR/SCons/site_scons/site_tools/boost_python.py
cp $RECIPE_DIR/python.py $SP_DIR/SCons/site_scons/site_tools/python.py
cp $RECIPE_DIR/nose.py $SP_DIR/SCons/site_scons/site_tools/nose.py

set +ve