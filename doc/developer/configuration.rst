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

.. _section-developer-configure:

Configure
#########

In order to ease the development of the **StatisKit** software suite on multiple operating systems, the **Conda** package and environment management system is used.
We here presents how to install the **Conda** package and environment management system and the :code:`statiskit-dev` environment within which you can build from source code the **StatisKit** software suite.

.. note::

    For more information concerning **Conda**, please refers to its `documentation <http://conda.pydata.org/docs>`_.

On windows
----------

In order to develop on Windows, you must first install `Visual Studio Community 2013 <https://www.visualstudio.com/en-us/news/releasenotes/vs2013-community-vs>`_.

Then, if you have a:

* 32-bit Windows OS, download the following `installer <https://github.com/StatisKit/StatisKit/raw/master/doc/win/32/developer_install.exe>`_.

* 64-bit Windows OS, download the following `installer <https://github.com/StatisKit/StatisKit/raw/master/doc/win/64/developer_install.exe>`_.

Then, open a shell in the directory where the installer was downloaded and type

.. code-block:: batch

    developer_install.exe

.. warning::

    If you already installed **Conda**, type instead

    .. code-block:: batch

        developer_install.exe --prefix=<path\to\conda>

    Where :code:`<path\to\conda>` has to replaced by the actual **Conda** directory.

.. note::

    More informations concerning this :code:`user_install.exe` installer can be obtained by typing

    .. code-block:: batch

        developer_install.exe -h 

On Linux and Mac OS X
---------------------

.. warning::

    For Unix OSes, we only provide 64-bit installers.
    If you have a 32-bit Unix OS, use type following commands

    .. code-block:: bash

        git clone https://gist.github.com/8a8b5ea835ac3cf5c46f8e02b31f6f34.git install-scripts
        cd install-scripts

    Then, replace :code:`./developer_install` by :code:`python developer_install.py` in the following recommendations.



If you have a:

* Linux OS, download the following `installer <https://github.com/StatisKit/StatisKit/raw/master/doc/linux/developer_install>`_.

* Mac OS X, download the following `installer <https://github.com/StatisKit/StatisKit/raw/master/doc/osx/developer_install>`_.

Then, open a shell in the directory where the installer was downloaded and type

.. code-block:: batch

    sudo chmod a+rwx developer_install
    ./developer_install

.. warning::

    If you already installed **Conda**, type instead

    .. code-block:: batch

        ./developer_install --prefix=<path/to/conda>

    Where :code:`<path/to/conda>` has to replaced by the actual **Conda** directory.

.. note::

    More informations concerning this :code:`developer_install` installer can be obtained by typing

    .. code-block:: batch

        ./developer_install -h 
        
        
.. note::

    This installation also install some plugins for build systems for the **Sublime Text** `software <https://www.sublimetext.com/3>`_.
