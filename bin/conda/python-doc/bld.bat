echo ON

pip install sphinxcontrib-blockdiag --install-option="--prefix=%PREFIX%"
if errorlevel 1 exit 1
pip install sphinx_rtd_theme --install-option="--prefix=%PREFIX%"
if errorlevel 1 exit 1
pip install chios --install-option="--prefix=%PREFIX%"
if errorlevel 1 exit 1

echo OFF