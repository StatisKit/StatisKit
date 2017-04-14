Install it !
############

.. _section-user-install_it-prerequisites:

Prerequisites
=============

In order to ease the installation of the **StatisKit** software suite on multiple operating systems, the **Conda** package and environment management system is used.
We here presents how to install the **Conda** package and environment management system.

.. note::

    For more information concerning **Conda**, please refers to its `documentation <http://conda.pydata.org/docs>`_.



On windows
----------

If you have a:

* 32-bit Windows OS, download the following `installer <https://github.com/StatisKit/StatisKit/raw/master/doc/win/32/user_install.exe>`_.

* 64-bit Windows OS, download the following `installer <https://github.com/StatisKit/StatisKit/raw/master/doc/win/64/user_install.exe>`_.

Then, open a shell in the directory where the installer was downloaded and type

.. code-block:: batch

    user_install.exe

.. warning::

    If you already installed **Conda**, type instead

    .. code-block:: batch

        user_install.exe --prefix=<path\to\conda>

    Where :code:`<path\to\conda>` has to replaced by the actual **Conda** directory.

.. note::

    More informations concerning this :code:`user_install.exe` installer can be obtained by typing

    .. code-block:: batch

        user_install.exe -h 

On Linux and Mac OS X
---------------------

.. warning::

    For Unix OSes, we only provide 64-bit installers.
    If you have a 32-bit Unix OS, use type following commands

    .. code-block:: bash

        git clone https://gist.github.com/8a8b5ea835ac3cf5c46f8e02b31f6f34.git install-scripts
        cd install-scripts

    Then, replace :code:`./user_install` by :code:`python user_install.py` in the following recommendations.



If you have a:

* Linux OS, download the following `installer <https://github.com/StatisKit/StatisKit/raw/master/doc/linux/user_install>`_.

* Mac OS X, download the following `installer <https://github.com/StatisKit/StatisKit/raw/master/doc/osx/user_install>`_.

Then, open a shell in the directory where the installer was downloaded and type

.. code-block:: batch

    sudo chmod a+rwx user_install
    ./user_install

.. warning::

    If you already installed **Conda**, type instead

    .. code-block:: batch

        ./user_install --prefix=<path\to\conda>

    Where :code:`<path\to\conda>` has to replaced by the actual **Conda** directory.

.. note::

    More informations concerning this :code:`user_install` installer can be obtained by typing

    .. code-block:: batch

        ./user_install -h 

Recommanded Installation
========================

To install **StatisKit**, open a new shell, choose an interface and proceed as detailled the corresponding section:

.. toctree::
    :maxdepth: 1

    c++
    python

.. warning::

    Depending on the precedent installation, **Conda** is likely to be inactivated.
    To solve this, on:
    
    * Windows, use the *Anaconda Prompt* shell in place of the *CMD* shell or, follow instructions available in :ref:`section-activate-conda` the section.
    * Linux and OS X, follow instructions available in :ref:`section-activate-conda` the section or use the :code:`--preprend-path=yes` option when runnning the installer.

Custom Installations
====================
    
For custom installations, **Conda** environments proposed in the :ref:`section-recommended-installation` section can be adapted to fit your purposes.
For example, if you consider the *Python* interface, the environment is described as follows:

.. remote-code-block:: yaml

    https://raw.githubusercontent.com/StatisKit/python-binder/master/environment.yml
    
If you want :

* To change the name of the environment in which this interface is installed (e.g. :code:`python` in place of :code:`python-statiskit`), replace the name field by the appropriate name using the following command in a shell:

  .. code-block:: console

    conda env update -n python statiskit/python-statiskit

* To remove a precise package of the environment, download the environment and remove the package name from the listing.
  If this package is mandatory for the packages you kept, don't worry, **Conda** will ensure that it is nevertheless installed. 
  
  .. note::
  
    You can download an environment with the :code:`anaconda-client`.
    If you don't have this package installed, it can be done using the following command line:
    
    .. code-block:: console
    
        conda install -n root anaconda-client
        
    Then, download the :code:`python-statiskit` environment using the following command line:
    
    .. code-block:: console
    
        anaconda download statiskit/python-statiskit
        
    Edit the :code:`environment.yml` file downloaded and install the resulting environment:
     
    .. code-block:: console

        conda env update

.. warning::

    If you are not in the same shell, **Conda** is likely to be inactivated.
    To reactivate it, follow instructions available in :ref:`section-activate-conda` the section.
