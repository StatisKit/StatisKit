set -xe

git clone https://github.com/pfernique/PkgTk.git
cd PkgTk/conda

conda build python-pkgtk -c statiskit -c conda-forge