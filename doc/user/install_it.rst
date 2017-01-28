Install it !
############

.. _section-user-install_it-prerequisites:

Prerequisites
=============

In order to ease the installation of this software suite on multiple operating systems, the **Conda** package and environment management system is used.

.. note::

    For more information concerning **Conda**, please refers to its `documentation <http://conda.pydata.org/docs>`_.

To install **Conda** on:

* Linux and OS X, download the following :download:`script <user_install.sh>`.
  Then, open a shell in the same directory and type the following command:

  .. code-block:: bash
    
        source user_install.sh

* Windows, download the following :download:`script <user_install.bat>`.
  Then, open a shell in the same directory and type the following command:

  .. code-block:: batch

        call user_install.bat

  .. note::

    You must install the `cURL <https://curl.haxx.se/download.html#Win32>`_ program for this script to work.
    If you are confused by code and have a compatible windows version (superior to 2000/XP), we recommend to use the installers present on this `website <http://www.confusedbycode.com/curl/>`_.
    In the worst case scenario, download in the same directory the installer of your choice from this page `miniconda <http://conda.pydata.org/miniconda.html>`_ (but do not run it), then execute the :code:`user_install.bat` file.

.. warning::

    Refers to the table :ref:`table-env-vars-users` to configure the script execution.
    If you already installed **Conda** you can, for example, type the following commands in a shell:
    
    * On Linux or OS X,

      .. code-block:: bash
      
        export CONDA_DIR=my/path/to/conda
        source user_install.sh
        
    * On Windows,
    
      .. code-block:: batch
      
        set CONDA_DIR=my\path\to\conda
        call user_install.bat
        
        
.. _table-env-vars-users:

.. table:: Environment variables for installation scripts
   :widths: auto

   +-----------------------+----------------------------------------------------------------------------------------------------------------+
   |    **CONDA_DIR**      | | The directory within which **Conda** will be installed (default is                                           |
   |                       | | :code:`$HOME/.miniconda$CONDA_VERSION` for Linux and OS X and                                                |
   |                       | | :code:`%USERPROFILE%\Miniconda%CONDA_VERSION%` for Windows). Note that                                       |
   |                       | | this directory is marked as hidden in Windows.                                                               |
   +-----------------------+----------------------------------------------------------------------------------------------------------------+
   |  **CONDA_VERSION**    | | The version of **Conda** to install (must be :code:`2` or :code:`3`, default is :code:`2`).                  |                                                       
   +-----------------------+----------------------------------------------------------------------------------------------------------------+
   | **CONDA_ALWAYS_YES**  | | Choose the :code:`yes` option whenever asked to proceed, such as when                                        |
   |                       | | installing (must be :code:`false` or :code:`true`, default is :code:`false`)                                 |
   +-----------------------+----------------------------------------------------------------------------------------------------------------+
   | **CONDA_CHANGE_PS1**  | | When using activate, change the command prompt ($PS1) to include                                             |
   |                       | | the activated environment (must be :code:`true` or :code:`false`, default is                                 |
   |                       | | :code:`true`).                                                                                               |
   +-----------------------+----------------------------------------------------------------------------------------------------------------+

.. _section-recommended-installation:

Recommanded Installation
========================

To install **StatisKit**, choose an interface and proceed as follows in the same shell:

.. toctree::
    :maxdepth: 1

    c++
    python

.. warning::

    If you are not in the same shell, depending on the precedent installation, **Conda** is likely to be inactivated.
    To solve this, on:
    
    * Windows, use the *Anaconda Prompt* shell in place of the *CMD* shell or, follow instructions available in :ref:`section-activate-conda` the section.
    * Linux and OS X, follow instructions available in :ref:`section-activate-conda` the section or, during the execution of :code:`user_install.sh`, answer :code:`yes` to the question 
    
      Do you wish the installer to prepend the Miniconda2 install location 
      to PATH in your ~/.bashrc ? [yes|no]

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
