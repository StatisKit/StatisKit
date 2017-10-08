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

Configure your Computer
#######################

In order to ease the development of the **StatisKit** software suite on multiple operating systems, the **Conda** package and environment management system is used.
To insall **Conda** refer to the section :ref:`_section-user-install_it-prerequisites`.

Once **Conda** installed, you need to create the development environment called :code:`statiskit-toolchain` on your machine.

.. warning::

    In order to develop on Windows, you must first install `Visual Studio Community 2013 <https://www.visualstudio.com/en-us/news/releasenotes/vs2013-community-vs>`_.

To do so:

1. Install :code:`conda-build-all` package in the :code:`root` environment.

   .. code-block:: bash

     conda install -n root conda-build-all -c conda-forge

2. Clone the :code:`StatisKit` repository of the :code:`StatisKit` organization.

   .. code-block:: bash

     git clone --recursive https://github.com/StatisKit/StatisKit.git

   .. note::

     If **git** is not installed on your computer, you can install it with conda:

     .. code-block:: bash

       conda install -n root git -c conda-forge

3. Build all **Conda** recipes available in this repository using :code:`conda-build-all`.
   
   * For the latest *Python 2* version
     
     .. code-block:: bash

       conda build-all StatisKit --matrix-conditions "python 2.*.*" --matrix-max-n-minor-versions 1 --no-inspect-conda-bld-directory

   * For the latest *Python 3* version
     
     .. code-block:: bash

       conda build-all StatisKit --matrix-conditions "python 3.*.*" --matrix-max-n-minor-versions 1 --no-inspect-conda-bld-directory

   .. note::
   
     If one build failed, you can re-use the previous commands.
     But, if you don't want to re-build successful builds, remove the :code:`--no-inspect-conda-bld-directory` option.
     
4. Install the :code:`statiskit-toolchain` package in an eponymous environment

    .. code-block:: bash

        conda create -n statiskit-toolchain statiskit-toolchain --use-local -c statiskit -c conda-forge

5. The created environment is to use for each build of **Statiskit** software suite.

    * For Windows OSes

        .. code-block:: bash

          activate statiskit-toolchain

    * For Unix OSes

        .. code-block:: bash

          source activate statiskit-toolchain
