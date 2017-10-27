set -ve

mkdir -p $PREFIX/etc/conda/activate.d
cp $RECIPE_DIR/activate.sh $PREFIX/etc/conda/activate.d/libtoolchain_vars.sh

mkdir -p $PREFIX/etc/conda/deactivate.d
cp $RECIPE_DIR/deactivate.sh $PREFIX/etc/conda/deactivate.d/libtoolchain_vars.sh

set +ve