set -xe

git clone https://github.com/StatisKit/Misc.git
cd Misc/conda

conda install python-pkgtk -c statiskit -c conda-forge
TOOLCHAIN=`pkgtk toolchain`

for CONDA_RECIPE in libboost python-scons python-parse; do
  conda build $CONDA_RECIPE -c statiskit
done
