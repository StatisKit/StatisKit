ARG CONDA_VERSION=2
ARG UBUNTU_VERSION=14.04
FROM i686/ubuntu:$UBUNTU_VERSION

ARG CONDA_VERSION

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install curl bzip2 -y

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
RUN git clone http://github.com/StatisKit/conda-tools
RUN git clone http://github.com/StatisKit/StatisKit
RUN cd StatisKit/bin/conda && conda build python-scons scons-tools libtoolchain python-toolchain --old-build-string
RUN cd conda-tools/bin/conda && conda build conda-tools --old-build-string
RUN conda install conda_tools --use-local
RUN git clone http://github.com/StatisKit/StatisKit
RUN conda release StatisKit