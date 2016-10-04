set -xe

conda install ipython jupyter

conda build toolchain -c statiskit
conda install toolchain --use-local -c statiskit
source activate $CONDA_DEFAULT_ENV

for CONDA_RECIPE in libboost_python python-scons python-parse; do
  conda build $CONDA_RECIPE -c statiskit
  conda install $CONDA_RECIPE --use-local -c statiskit
done
