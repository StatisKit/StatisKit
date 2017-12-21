set -ve

conda install vcs \
              ipython \
              jupyter \
              conda-build \
              anaconda-client \
              conda-tools \
              python-softmaint \
              python-autowig \
              python-clanglite \
              --use-local \
              -c statiskit \

set +ve
