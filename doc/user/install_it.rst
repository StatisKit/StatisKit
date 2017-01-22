Install it !
############

.. _section-user-install_it-prerequisites:

Prerequisites
=============

In order to ease the installation of this software suite on multiple operating systems, the **Conda** package and environment management system is used.

.. note::

    For more information concerning **Conda**, please refers to its `documentation <http://conda.pydata.org/docs>`_.

To install **Conda** on:

* Linux and OS X, download the following :download:`script <install.sh>`.
  Then, open a shell in the same directory and type the following command:

  .. code-block:: bash
    
        source install.sh

* Windows, download the following :download:`script <install.bat>`.
  Then, open a shell in the same directory and type the following command:

  .. code-block:: batch

        call install.bat

  .. note::

    You must install the `cURL <https://curl.haxx.se/download.html#Win32>`_ program for this script to work.
    If you are confused by code and have a compatible windows version (superior to 2000/XP), we recommend to use the installers present on this `website <http://www.confusedbycode.com/curl/>`_.

.. warning::

    Refers to the table :ref:`table-env-vars-users` to configure the script execution.
    If you already installed **Conda** you can, for example, type the following commands in a shell:
    
    * On Linux or OS X,

      .. code-block:: bash
      
        export CONDA_DIR=my/path/to/conda
        source install.sh
        
    * On Windows,
    
      .. code-block:: batch
      
        set CONDA_DIR=my\path\to\conda
        call install.bat
        
        
.. _table-env-vars-users:

.. table:: Environment variables for installation scripts
   :widths: auto

   +-----------------------+----------------------------------------------------------------------------------------------------------------+
   |    **CONDA_DIR**      | | The directory within which **Conda** will be installed (default is                                           |
   |                       | | :code:`$HOME/.miniconda$CONDA_VERSION` for Linux and OS X and :code:`%USERPROFILE%\Miniconda%CONDA_VERSION%` |
   |                       | | for Windows). Note that this directory is marked as hidden in Windows.                                       |
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

    If you are not in the same shell, **Conda** is likely to be inactivated.
    To reactivate it, follow instructions available in :ref:`section-activate-conda` the section.

Custom Installations
====================

For custom installations, **Conda** environments proposed in the :ref:`section-recommended-installation` section can be adapted to fit your purposes.
For example, if you consider the *Python* interface, the default environment is described as follows:

.. remote-code-block:: yaml

    https://raw.githubusercontent.com/StatisKit/python-binder/master/environment.yml
    
If you want :

* To change the name of the environmentin which this interface is installed, replace the name field the appropriate name.
* To remove a precise package of the environment (for instance :code:`python-statiskit_glm`), remove it in the listing.
  If this package is mandatory for the packages you kept, don't worry, **Conda** will ensure that it is nevertheless installed. 
  
  .. remote-code-block:: yaml
  
    https://raw.githubusercontent.com/StatisKit/python-binder/master/environment.yml
