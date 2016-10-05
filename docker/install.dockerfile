FROM statiskit/ubuntu

# Install libraries and packages from Misc
RUN git clone https://github.com/Statiskit/Misc.git $HOME/Misc
RUN cd $HOME/Misc/conda && bash install.sh

WORKDIR /home/main

