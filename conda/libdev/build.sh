set -ve

cp $RECIPE_DIR/cpp.py $SP_DIR/SCons/site_scons/site_tools/cpp.py
cp $RECIPE_DIR/libdev_vars.sh $PREFIX/etc/conda/activate.d/libdev_vars.sh

set +ve