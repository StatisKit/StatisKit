export STK_SP_DIR=`python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"`
export SCONSFLAGS=$SCONSFLAGS --site-dir=$STK_SP_DIR/scons_tools