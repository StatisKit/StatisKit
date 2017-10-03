set -ve

export TMP_DIR=`python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`
if [[ "$SCONSFLAGS" = "" ]]; then
    export SCONSFLAGS=$SCONSFLAGS --site-dir=$TMP_DIR/scons_tools
else
    export SCONSFLAGS=--site-dir=$TMP_DIR/scons_tools
fi
unset TMP_DIR

set +ve