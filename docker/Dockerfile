FROM statiskit/ubuntu

# Update the OS
RUN apt-get update

# Upgrade the OS
RUN apt-get -y upgrade

# Install useful tools
RUN apt-get install -y vim build-essential git wget curl
# firefox
RUN apt-get autoremove

# Add user for future work
RUN useradd -m main --shell /bin/bash && echo "main:main" | chpasswd && adduser main sudo

# select created user
USER main

ENV PATHBACK $PATH

# Install miniconda2
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh \
         -O $HOME/miniconda2.sh
RUN bash $HOME/miniconda2.sh -b -p $HOME/miniconda2
RUN rm $HOME/miniconda2.sh
RUN touch $HOME/miniconda2.sh
RUN echo 'export PATH=$HOME/miniconda2/bin:$PATHBACK' >> $HOME/miniconda2.sh
RUN echo 'source $HOME/miniconda2/bin/activate' >> $HOME/miniconda2.sh
ENV PATH /home/main/miniconda2/bin:$PATHBACK
RUN conda config --set always_yes yes --set changeps1 no
RUN conda update -q conda
RUN conda info -a
RUN conda install conda-build anaconda-client ipython jupyter
RUN mkdir $HOME/miniconda2/conda-bld
RUN mkdir $HOME/miniconda2/conda-bld/linux-64

# Install miniconda3
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh \
         -O $HOME/miniconda3.sh
RUN bash $HOME/miniconda3.sh -b -p $HOME/miniconda3
RUN rm $HOME/miniconda3.sh
RUN touch $HOME/miniconda3.sh
RUN echo 'export PATH=$HOME/miniconda3/bin:$PATHBACK' >> $HOME/miniconda3.sh
RUN echo 'source $HOME/miniconda3/bin/activate' >> $HOME/miniconda3.sh
ENV PATH /home/main/miniconda3/bin:$PATHBACK
RUN conda config --set always_yes yes --set changeps1 no
RUN conda update -q conda
RUN conda info -a
RUN conda install conda-build anaconda-client ipython jupyter
RUN mkdir $HOME/miniconda3/conda-bld
RUN mkdir $HOME/miniconda3/conda-bld/linux-64

ENV PATH /home/main/miniconda2/bin:$PATHBACK

RUN git clone https://gist.github.com/93e0375712c6e62f76bec455e89d0437.git $HOME/git-config
RUN cd $HOME/git-config && bash git-config.sh
RUN rm -rf $HOME/git-config

#jupyter notebook --ip='*' --port=8888 --no-browser
#You can then view the Jupyter Notebook by opening http://localhost:8888 in your browser, or http://<DOCKER-MACHINE-IP>:8888 if you are using a Docker Machine VM.
WORKDIR /home/main
