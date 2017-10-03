set -ve

export TMP_DIR=`python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`
export SCONSFLAGS=$SCONSFLAGS --site-dir=$TMP_DIR/scons_tools
unset TMP_DIR

set +ve