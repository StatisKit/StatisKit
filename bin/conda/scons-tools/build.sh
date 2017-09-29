set -ve

mkdir -p $PREFIX/etc/conda/activate.d
cp $RECIPE_DIR/activate.sh $PREFIX/etc/conda/activate.d/scons_vars.sh

mkdir -p $PREFIX/etc/conda/deactivate.d
cp $RECIPE_DIR/deactivate.sh $PREFIX/etc/conda/activate.d/scons_vars.sh

export TGT_DIR=scons_tools
mkdir $SP_DIR/$TGT_DIR
touch $SP_DIR/$TGT_DIR/__init__.py

for SCONS_TOOL in `ls *.py`; do
    if [[ "$PY3K" = "1" ]]; then
        2to3 -n -w $SCONS_TOOL
    fi
    cp $SCONS_TOOL $SP_DIR/$TGT_DIR/$SCONS_TOOL
done

set +ve