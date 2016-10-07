set -xe

conda install ipython jupyter
conda install libboost --use-local -c statiskit -c conda-forge
conda install python-scons --use-local -c statiskit -c conda-forge