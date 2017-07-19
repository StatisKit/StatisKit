Test it !
#########

In a first stage, you are not compelled to install **StatisKit** on your computer in order to discover its functionalities.
Using **Docker** images and **Binder** servers and **Jupyter** notebooks, we are able to provide pre-installed interfaces with various examples.

.. note::

    For more information refers to :
    
    * The **Jupyter** `documentation <https://jupyter.readthedocs.io/en/latest/index.html>`_.
    * The **Binder** `documentation <http://docs.mybinder.org/>`_.
    * The **Docker** `documentation <https://docs.docker.com/>`_.
    
Online with **Binder**
======================

Test the latest *Python* interface on this `server <http://mybinder.org/repo/statiskit/python-binder>`_.

.. warning::

    **Binder** servers might be outdated but can be updated using links available on the following repository `python-binder <https://github.com/StatisKit/python-binder>`_.
    
On your computer with **Docker**
================================

Test the latest *Python* interface with this `image <https://hub.docker.com/r/statiskit/python/tags>`_.
After `installing <https://docs.docker.com/engine/installation/>`_ **Docker**, you can type the following commands in a shell:

.. code-block:: console

    docker run -i -t -p 8888:8888 statiskit/python:latest
    jupyter notebook index.ipynb --ip='*' --port=8888 --no-browser
   
You can then view the **Jupyter** notebooks by opening http://localhost:8888/notebooks/index.ipynb in your browser, or http://<DOCKER-MACHINE-IP>:8888/notebooks/index.ipynb if you are using a Docker Machine VM (see this `documentation <https://docs.docker.com/machine/>`_ for more informations).

.. warning::

    By default, on some operating systems like Ubuntu, docker require to have administration rights.
    You can, for example, execute the preceeding lines after typing :code:`sudo -i` if you are on Ubuntu or follow these `instructions <https://docs.docker.com/engine/installation/linux/linux-postinstall/>`_.
    
On your computer from a SSH server
==================================

Test the latest *Python* interface installed on a ssh server.

.. note::

    The username on the ssh server (resp. the ssh servername) is denoted in the following by :code:`<username>` (resp. :code:`<servername>`).
    Please replace it by the appropriate username (resp. servername).
    
You can type the following commands in a shell:

.. code-block:: console

    ssh -L 8888:localhost:8888 <username>@<servername>
    jupyter notebook --ip='*' --port=8888 --no-browser
    
Then, access to the URL provided in the terminal, from your computer web browser.
