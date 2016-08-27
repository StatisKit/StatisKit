FROM ubuntu:14.04

# Build or install
ARG BUILD="true"

# RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list

# Update the OS
RUN apt-get update

# Upgrade the OS
RUN apt-get -y upgrade

# Install useful tools
RUN apt-get install -y vim build-essential git wget
# firefox
RUN apt-get autoremove

# Add user for future work
RUN useradd -ms /bin/bash main

# select created user
USER main

# Install miniconda
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O \ 
  $HOME/miniconda.sh
RUN bash $HOME/miniconda.sh -b -p $HOME/miniconda
RUN rm $HOME/miniconda.sh
ENV PATH /home/main/miniconda/bin:$PATH
RUN echo 'export PATH=$PATH:$HOME/miniconda/bin' >> $HOME/.bashrc 
RUN conda config --set always_yes yes --set changeps1 no
RUN conda update -q conda
RUN conda info -a

# Install conda-build
RUN conda install conda-build==1.21.7

# Install IPython, Jupyter and Pip
RUN conda install ipython jupyter pip

# Install libraries and packages from Misc
## Clone the repository
RUN [ $BUILD = "true" ] && git clone https://github.com/Statiskit/Misc.git $HOME/Misc || [ $BUILD = "false" ]

## Create a file for anaconda upload
RUN [ -f $HOME/post-link.sh ] && head -n -5 $HOME/post-link.sh || touch $HOME/post-link.sh && echo "set -e" >> $HOME/post-link.sh
RUN echo "set -e" >> $HOME/post-link.sh
RUN [ $BUILD = "true" ] && echo "$HOME/miniconda/bin/conda install anaconda-client" >> $HOME/post-link.sh || [ $BUILD = "false" ]

## Build libboost recipe
RUN [ $BUILD = "true" ] && $HOME/miniconda/bin/conda build $HOME/Misc/libboost -c statiskit || [ $BUILD = "false" ]

## Build python-scons recipe
RUN [ $BUILD = "true" ] && $HOME/miniconda/bin/conda build $HOME/Misc/python-scons -c statiskit || [ $BUILD = "false" ]

## Build python-parse recipe
RUN [ $BUILD = "true" ] && $HOME/miniconda/bin/conda build $HOME/Misc/python-parse -c statiskit || [ $BUILD = "false" ]

# Create a file for anaconda post-link
RUN [ $BUILD = "true" ] && echo "conda install anaconda-client" >> $HOME/post-link.sh || [ $BUILD = "false" ]
RUN [ $BUILD = "true" ] && echo "anaconda upload \`conda build $HOME/Misc/libboost --output\` --user statiskit --force" >> $HOME/upload.sh || [ $BUILD = "false" ]
RUN [ $BUILD = "true" ] && echo "anaconda upload \`conda build $HOME/Misc/python-scons --output\` --user statiskit --force" >> $HOME/upload.sh || [ $BUILD = "false" ]
RUN [ $BUILD = "true" ] && echo "anaconda upload \`conda build $HOME/Misc/python-parse --output\` --user statiskit --force" >> $HOME/upload.sh || [ $BUILD = "false" ]
RUN ( [ $BUILD = "true" ] && for recipe in Misc/*/; do echo "anaconda upload \`conda build" $recipe "--output\` --user statiskit --force" >> $HOME/post-link.sh; done; ) || [ $BUILD = "false" ]
RUN [ $BUILD = "false" ] && echo "rm -rf Misc" >> $HOME/post-link.sh || [ $BUILD = "true" ]
RUN [ $BUILD = "true" ] && echo "conda remove anaconda-client" >> $HOME/post-link.sh || [ $BUILD = "false" ]
RUN [ $BUILD = "true" ] && echo "conda env remove -n _build" >> $HOME/post-link.sh || [ $BUILD = "false" ]
RUN [ $BUILD = "true" ] && echo "conda env remove -n _test" >> $HOME/post-link.sh || [ $BUILD = "false" ]
RUN echo "conda clean --all" >> $HOME/post-link.sh
RUN echo "rm $HOME/post-link.sh" >> $HOME/post-link.sh
RUN [ $BUILD = "false" ] && cd $HOME && /bin/bash post-link.sh || [ $BUILD = "true" ]

WORKDIR /home/main
