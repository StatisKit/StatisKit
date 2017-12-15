ARG CONDA_VERSION=2
ARG UBUNTU_VERSION=14.04
FROM i686/ubuntu:$UBUNTU_VERSION

ARG CONDA_VERSION

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install curl bzip2 build-essential -y

RUN useradd -m main --shell /bin/bash && echo "main:main" | chpasswd && adduser main sudo
USER main
WORKDIR /home/main

RUN curl "https://repo.continuum.io/miniconda/Miniconda"$CONDA_VERSION"-latest-Linux-x86.sh" -o miniconda.sh
RUN chmod a+rwx miniconda.sh
RUN ./miniconda.sh -b -p /home/main/miniconda
RUN rm miniconda.sh
env PATH /home/main/miniconda:/home/main/miniconda/bin:$PATH
RUN chmod -R a+rwx /home/main/miniconda
RUN conda config --set always_yes yes
RUN conda install git conda-build anaconda-client
# RUN conda install vcs ipython jupyter conda-build anaconda-client -c statiskit -c conda-forge
RUN git clone --recursive http://github.com/StatisKit/StatisKit
RUN cd StatisKit/bin/conda && conda build python-scons scons-tools libtoolchain python-toolchain --old-build-string
RUN cd StatisKit/share/git/ClangLite/bin/conda && git pull origin master
RUN cd StatisKit/share/git/ClangLite/bin/conda && conda build llvm clang libclanglite python-clanglite --old-build-string
RUN cd StatisKit/share/git/AutoWIG/bin/conda && conda build python-autowig --old-build-string
RUN for filename in $CONDA_PREFIX/conda-bld/linux-32/*; do anaconda upload $filename -u statiskit --label docker_release; done