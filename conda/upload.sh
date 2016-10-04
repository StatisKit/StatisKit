[[ ! "$ANACONDA_USERNAME"=="" ]] || read -p "Username: " ANACONDA_USERNAME
[[ ! "$ANACONDA_PASSWORD"=="" ]] || read -s -p %ANACONDA_USERNAME"'s password: " ANACONDA_PASSWORD

set -x

conda install -y -n root anaconda-client;
yes | anaconda login --username "$ANACONDA_USERNAME" --password "$ANACONDA_PASSWORD"

for CONDA_RECIPE in python-pkgtk; do
  CONDA_FILE=`conda build $CONDA_RECIPE --output`
  anaconda upload --user statiskit ${CONDA_FILE%%} || echo "upload failed"
done

anaconda logout