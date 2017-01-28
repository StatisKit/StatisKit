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

In order to ease the development of this software suite on multiple operating systems, the **Conda** package and environment management system is used.

.. warning::

    These scripts use scripts presented in the :ref:`section-user-install_it-prerequisites` section, there are therefore no need to run these scripts beforehand.
    Nevertheless, refers to the :ref:`section-user-install_it-prerequisites` section to configure the following script executions.

To install **Conda** and the development environment on:

* Linux and OS X, download the following :download:`script <developer_install.sh>`.
  Then, open a shell in the same directory and type the following command:

  .. code-block:: bash
    
        source developer_install.sh

* Windows, download the following :download:`script <developer_install.bat>`.
  Then, open a shell in the same directory and type the following command:

  .. code-block:: batch

        call developer_install.bat

Afterwards, the `statiskit-dev <https://raw.githubusercontent.com/StatisKit/StatisKit/master/conda/statiskit-dev.yml>`_ environment is installed and you can activate it by typing in the same shell:

* On Linux and OS X, 

  .. code-block:: console

      source activate statiskit-dev

* On windows, 

  .. code-block:: console

      activate statiskit-dev


If you want to configure your favorite editor:

* to be used with **Git**,
* to be able to use **SCons** from within.

Download and execute the following scripts for:

* The **Sublime Text** `software <https://www.sublimetext.com/3>`_ :download:`on Linux and OS X <sublime_text.sh>`.
* The **gedit** `software <https://wiki.gnome.org/Apps/Gedit>`_ :download:`on Linux and OS X <gedit.sh>`.
  
  .. todo::
  
    Cannot use **SCons** from within.

.. warning::

    The chosen script must be executed -- in the same way as before -- in the same shell as the one used for the :code:`developer_install.sh` or :code:`developer_install.bat` scripts.
