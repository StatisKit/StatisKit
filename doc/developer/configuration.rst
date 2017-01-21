.. ................................................................................ ..
..                                                                                  ..
..  StatisKit: meta-repository providing general documentation and tools for the    ..
..  **StatisKit** Organization                                                      ..
..                                                                                  ..
..  Copyright (c) 2016 Pierre Fernique                                              ..
..                                                                                  ..
..  This software is distributed under the CeCILL-C license. You should have        ..
..  received a copy of the legalcode along with this work. If not, see              ..
..  <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                  ..
..                                                                                  ..
..  File authors: Pierre Fernique <pfernique@gmail.com> (11)                        ..
..                                                                                  ..
.. ................................................................................ ..

Configuration
#############

In order to ease the development of this software suite on multiple operating systems, some tools have to be installed.

To install this tools on:

* Linux and OSX, download the following :download:`script <install.sh>`.
  Then, open a shell in the same directory and type the following command:

  .. code-block:: bash
    
        source install.sh

* Windows, download the following :download:`script <install.bat>`.
  Then, open a shell in the same directory and type the following command:

  .. code-block:: batch

        call install.bat

.. warning::

    Refers to the :ref:`section-user-install_it-prerequisites` and the table :ref:`table-env-vars-developpers` to configure the script execution.

.. _table-env-vars-developpers:

.. table:: Environment variables for installation scripts
   :widths: auto

   +-----------------------+---------------------------------------------------------------------------------------------------------------+
   |    **CONDA_DIR**      | | The directory within which **Conda** will be installed (default is                                          |
   |                       | | :code:`$HOME/.miniconda$CONDA_VERSION` for Linux and OSX and                                                |
   |                       | :code:`%USERPROFILE%\Miniconda%CONDA_VERSION%` for Windows).                                                  |
   |                       |                                                                                                               |
   |                       | Note that this directory is marked as hidden in Windows.                                                      |
   +-----------------------+---------------------------------------------------------------------------------------------------------------+
   |  **CONDA_VERSION**    | | The version of **Conda** to install (must be :code:`2` or :code:`3`, default is :code:`2`).                 |                                                       
   +-----------------------+---------------------------------------------------------------------------------------------------------------+
   | **CONDA_ALWAYS_YES**  | | Choose the :code:`yes` option whenever asked to proceed, such as when                                       |
   |                       | | installing (must be :code:`false` or :code:`true`, default is :code:`false`)                                |
   +-----------------------+---------------------------------------------------------------------------------------------------------------+
   | **CONDA_CHANGE_PS1**  | | When using activate, change the command prompt ($PS1) to include                                            |
   |                       | | the activated environment (must be :code:`true` or :code:`false`, default is                                |
   |                       | | :code:`true`).                                                                                              |
   +-----------------------+---------------------------------------------------------------------------------------------------------------+