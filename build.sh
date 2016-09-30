set -xe

conda install ipython jupyter

conda build toolchain -c statiskit
conda install toolchain --use-local -c statiskit
source activate $CONDA_DEFAULT_ENV

conda build libboost-python -c statiskit
conda install libboost-python --use-local -c statiskit

conda build python-scons -c statiskit
conda install python-scons --use-local -c statiskit

conda build python-parse -c statiskit
conda install python-parse --use-local -c statiskit
