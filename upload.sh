set -x

conda install -n root anaconda-client;
yes | anaconda login --username "$ANACONDA_USERNAME" --password "$ANACONDA_PASSWORD"
source activate;
for CONDA_RECIPE in toolchain libboost_python python-scons python-parse; do
  CONDA_FILE=`conda build $CONDA_RECIPE --output`
  anaconda upload --user statiskit ${CONDA_FILE%%} || echo "upload failed"
done
anaconda logout
