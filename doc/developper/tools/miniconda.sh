if [[ ! "$CONDA_VERSION = "" ]]; then
  CONDA_VERSION=2
fi
wget https://repo.continuum.io/miniconda/Miniconda$CONDA_VERSION-latest-Linux-x86_64.sh miniconda.sh
if [[ -z CONDA_PATH = "" ]]; then
  CONDA_PATH=`pwd`
fi
bash miniconda.sh -b -p $CONDA_PATH/miniconda
rm miniconda.sh
export PATH=$CONDA_PATH/miniconda/bin:$PATH
if [[ ! "$CONDA_ALWAYS_YES = "" ]]; then
  CONDA_ALWAYS_YES=no
fi
if [[ ! "$CONDA_CHANGE_PS1 = "" ]]; then
  CONDA_CHANGE_PS1=yes
fi
conda config --set always_yes $CONDA_ALWAYS_YES --set changeps1 $CONDA_CHANGE_PS1
if [[ ! "$CONDA_BUILD_ROOT_DIR" = "" ]]; then
  echo "conda-build:" >> $HOME/.condarc;
  echo "  root-dir: " $CONDA_BUILD_ROOT_DIR >> $HOME/.condarc;
fi
conda update -q conda
conda info -a
conda install conda-build
conda install anaconda-client
if [[ "$AUTOENV" = "" ]]; then
  AUTOENV=yes
fi
if [[ "$AUTOENV" = "yes" ]]; then
  pip install autoenv
fi 
