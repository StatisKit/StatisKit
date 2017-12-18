ARG CONDA_VERSION=2
ARG UBUNTU_VERSION=14.04
FROM i686/ubuntu:$UBUNTU_VERSION

ARG CONDA_VERSION

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install wget curl bzip2 build-essential -y
RUN apt-get purge 
RUN apt-get clean

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
RUN echo "source activate root" >> .bashrc

RUN echo "set -ve" > build.sh
RUN echo "git clone --recursive http://github.com/StatisKit/StatisKit" >> build.sh
RUN echo "cd StatisKit/bin/conda" >> build.sh
RUN echo "conda build python-scons scons-tools libtoolchain python-toolchain boost-suite boost-meta python-parse --old-build-string" >> build.sh
RUN echo "cd ../../share/git/ClangLite/bin/conda" >> build.sh
RUN echo "conda build llvm clang libclanglite python-clanglite --old-build-string" >> build.sh
RUN echo "cd ../../../AutoWIG/bin/conda" >> build.sh
RUN echo "conda build python-autowig --old-build-string" >> build.sh
RUN echo "set +ve" >> build.sh

RUN echo "set -ve" > upload.sh

RUN echo "for filename in \$CONDA_PREFIX/conda-bld/linux-32/*.tar.bz2; do anaconda upload \$filename -u statiskit --label linux-32_release; done" > upload.sh
RUN echo "set +ve" >> upload.sh

RUN echo "set -ve" > install.sh
RUN echo "conda install vcs ipython jupyter conda-build anaconda-client conda-tools python-softmaint python-autowig python-clanglite -c statiskit -c conda-forge" > install.sh
RUN echo "set +ve" >> install.sh