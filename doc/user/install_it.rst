Install it !
############

Prerequisites
=============

In order to ease the installation of this software suite on multiple operating systems, the **Conda** package and environment management system is used.

.. note::

    For more information concerning **Conda**, please refers to its `documentation <http://conda.pydata.org/docs>`_.

To install **Conda** on:

* Linux and OSX, download the following :download:`script <install.sh>`.
  Then, open a terminal in the same directory and type the following command:

    .. code-block:: bash
    
        source install.sh


* Windows, download the following :download:`script <install.bat>`.
  Then, open a terminal in the same directory and type the following command:

    .. code-block:: batch

        call install.bat

.. warning::

    For more information concerning **Conda**, please refers to its `documentation <http://conda.pydata.org/docs>`_.
    Reports to the table :ref:`table-env-vars-scripts` to configure the script execution.

.. _table-env-vars-scripts:

.. table:: Environment variables for installation scripts
   :widths: auto

   +-------------------+-------------------------------------------------------------+
   |    CONDA_DIR      | | The directory within which **Conda** will be installed    |
   |                   | | (default is :code:`$HOME/miniconda`).                     |
   +-------------------+-------------------------------------------------------------+
   |  CONDA_VERSION    | | The version of **Conda** to install (must be :code:`2`    |
   |                   | | or :code:`3`, default is :code:`2`).                      |                                                       
   +-------------------+-------------------------------------------------------------+
   | CONDA_ALWAYS_YES  | | Choose the :code:`yes` option whenever asked to proceed,  |
   |                   | | such as when installing (must be :code:`"false"` or       |
   |                   | | :code:`"true"`, default is :code:`"false"`)               |
   +-------------------+-------------------------------------------------------------+
   | CONDA_CHANGE_PS1  | | When using activate, change the command prompt ($PS1) to  |
   |                   | | include the activated environment (must be :code:`"true"` |
   |                   | | or :code:`"false"`, default is :code:`"true"`).           |
   +-------------------+-------------------------------------------------------------+

.. _section-recommended-installation:

Recommanded Installation
========================

To use **StatisKit**, choose an interface:

.. toctree::
    :maxdepth: 1

    interfaces/c++
    interfaces/python

Custom Installations
====================

For custom installations, please refers individually to each **StatisKit** software suite component documentation.

.. note::

    **Conda** environments proposed in the :ref:`section-recommended-installation` section can be adapted to fit your purposes.