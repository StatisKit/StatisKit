conda install ipython jupyter

conda build libboost -c statiskit
conda install libboost --use-local -c statiskit

conda build python-scons -c statiskit
conda install python-scons --use-local -c statiskit

conda build python-parse -c statiskit
conda install python-parse --use-local -c statiskit
