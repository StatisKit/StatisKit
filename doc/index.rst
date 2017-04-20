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

Documentation
=============

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

Software
========

The **StatisKit** software suite is composed of multiple software

.. blockdiag::
    :align: center
    :desctable:
    
    blockdiag {
        orientation = portrait;
        
        A [label = "STL", shape="roundedbox",
           description="Minimal interpreted interfaces for the STL containers C++ template library.
                        Follow this `link <http://statiskit.rtfd.io/projects/STL>`_ for details."];
        B [label = "LinAlg", shape="roundedbox",
           description="Minimal interpreted interfaces for the Eigen C++ template library.
                        Follow this `link <http://statiskit.rtfd.io/projects/LinAlg>`_ for details."];
        C [label = "Core", shape="roundedbox",
           description="Classical statistical analyses for univariate and multivariate data.
                        Follow this `link <http://statiskit.rtfd.io/projects/Core>`_ for details."];
        D [label = "GLM", shape="roundedbox",
           description="Todo.
                        Follow this `link <http://statiskit.rtfd.io/projects/GLM>`_ for details."];
        E [label = "PGM", shape="roundedbox",
           description="Todo.
                        Follow this `link <http://statiskit.rtfd.io/projects/PGM>`_ for details."];
        
        A -> C;
        B -> C;
        C -> D;
        C -> E;

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
