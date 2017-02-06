set -ve

pip install sphinxcontrib-blockdiag --install-option="--prefix=$PREFIX"
pip install sphinx_rtd_theme --install-option="--prefix=$PREFIX"
pip install chios --install-option="--prefix=$PREFIX"

set +ve