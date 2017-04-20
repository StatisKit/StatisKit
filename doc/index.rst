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
..  File authors: Pierre Fernique <pfernique@gmail.com> (13)                        ..
..                                                                                  ..
.. ................................................................................ ..

.. include:: ../README.rst

General documentation
=====================

This documentation is dedicated to people using the **StatisKit** software suite.
In this documentation, the following expressions shall have the following meaning:

User
    means any individual using binary files originating from the compilation of the source code.

Developer
    means any individual modifying the source code for producing new binary files.

Maintener
    means any individual publishing new binary files from modified source code.

Please, with regard to previous expressions, refers to the subsequent guides.

.. toctree::
    :maxdepth: 2

    user/index
    developer/index.rst
    maintener/index.rst

Software specific documentation
===============================

The **StatisKit** software suite is composed of multiple software.
The following diagram presents dependency relations among software included in the **StatisKit** software suite.
For each software, its specific documentation can be found following the available link denoted by |LINK|.

.. |LINK| unicode:: U+1F517

.. |STL| unicode:: U+1F517
.. _STL: http://statiskit.rtfd.io/projects/STL

.. |LINALG| unicode:: U+1F517
.. _LINALG: http://statiskit.rtfd.io/projects/LinAlg

.. |CORE| unicode:: U+1F517
.. _CORE: http://statiskit.rtfd.io/projects/CORE

.. |GLM| unicode:: U+1F517
.. _GLM: http://statiskit.rtfd.io/projects/GLM

.. |PGM| unicode:: U+1F517
.. _PGM: http://statiskit.rtfd.io/projects/PGM

.. |DTP| unicode:: U+1F517
.. _DTP: http://statiskit.rtfd.io/projects/DTP

.. blockdiag::
    :align: center
    :desctable:
    
    blockdiag {
        orientation = portrait;
        
        A [label = "STL", shape="roundedbox",
           description="Minimal interpreted interfaces for the STL containers C++ template library |STL|_"];
        B [label = "LinAlg", shape="roundedbox",
           description="Minimal interpreted interfaces for the Eigen C++ template library |LINALG|_"];
        C [label = "Core", shape="roundedbox",
           description="Classical statistical analyses for univariate and multivariate data |CORE|_"];
        D [label = "GLM", shape="roundedbox",
           description="Todo |GLM|_"];
        E [label = "PGM", shape="roundedbox",
           description="Todo |PGM|_"];
                        
        F [label = "DTP", shape="roundedbox",
           description="Todo |DTP|_"];
        
        A -> C;
        B -> C;
        C -> D;
        C -> E;
        E -> F;

    }

License
=======

StatisKit is distributed under the |LICENSENAME|_.

.. note:: 

    |LICENSENAME| is GPL compatible.


Authors
=======

.. include:: ../AUTHORS.rst

.. |LICENSENAME| replace:: CeCILL license

.. _LICENSENAME : license.html

.. |LICENSE| replace:: see `License`_ section

.. |AUTHORS| replace:: see `Authors`_ section
