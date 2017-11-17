.. Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ..
..                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
.. Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
..                                                                       ..
.. This file is part of the AutoWIG project. More information can be     ..
.. found at                                                              ..
..                                                                       ..
..     http://autowig.rtfd.io                                            ..
..                                                                       ..
.. The Apache Software Foundation (ASF) licenses this file to you under  ..
.. the Apache License, Version 2.0 (the "License"); you may not use this ..
.. file except in compliance with the License. You should have received  ..
.. a copy of the Apache License, Version 2.0 along with this file; see   ..
.. the file LICENSE. If not, you may obtain a copy of the License at     ..
..                                                                       ..
..     http://www.apache.org/licenses/LICENSE-2.0                        ..
..                                                                       ..
.. Unless required by applicable law or agreed to in writing, software   ..
.. distributed under the License is distributed on an "AS IS" BASIS,     ..
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or       ..
.. mplied. See the License for the specific language governing           ..
.. permissions and limitations under the License.                        ..

.. include:: ../README.rst

General documentation
=====================

This documentation is dedicated to people using the **StatisKit** software suite.
In this documentation, the following expressions shall have the following meaning:

User
    means any individual using binary files originating from the compilation of the source code.

Developer
    means any user modifying the source code for producing new binary files.

Maintener
    means any developer publishing new binary files from modified source code.

Please, with regard to previous expressions, refers to the subsequent guides.
More insights on the project can be found on the organization **GitHub** `page <http://github.com/StatisKit>`_

.. toctree::
    :maxdepth: 3

    user/index
    developer/index.rst
    maintener/index.rst

Software specific documentation
===============================

The **StatisKit** software suite is composed of multiple software.
.. The following diagram presents dependency relations among software included in the **StatisKit** software suite.
.. For each software, its specific documentation can be found following the available link denoted by |LINK|.

.. .. |LINK| unicode:: U+1F517

.. .. |STL| unicode:: U+1F517
.. .. _STL: http://statiskit.rtfd.io/projects/STL

.. .. |LINALG| unicode:: U+1F517
.. .. _LINALG: http://statiskit.rtfd.io/projects/LinAlg

.. .. |CORE| unicode:: U+1F517
.. .. _CORE: http://statiskit.rtfd.io/projects/CORE

.. .. |GLM| unicode:: U+1F517
.. .. _GLM: http://statiskit.rtfd.io/projects/GLM

.. .. |PGM| unicode:: U+1F517
.. .. _PGM: http://statiskit.rtfd.io/projects/PGM

.. .. |DTP| unicode:: U+1F517
.. .. _DTP: http://statiskit.rtfd.io/projects/DTP

.. .. blockdiag::
..     :align: center
..     :desctable:
    
..     blockdiag {
..         orientation = portrait;

..         A [label = "STL", shape="roundedbox",
..            description="Minimal Interpreted Interfaces for the STL Containers C++ Template Library |STL|_"];
..         B [label = "LinAlg", shape="roundedbox",
..            description="Minimal Interpreted Interfaces for the Eigen C++ Template Library |LINALG|_"];
..         C [label = "Core", shape="roundedbox",
..            description="Classical statistical analyses for univariate and multivariate data |CORE|_"];
..         D [label = "GLM", shape="roundedbox",
..            description="Todo |GLM|_"];
..         E [label = "PGM", shape="roundedbox",
..            description="Todo |PGM|_"];
                        
..         F [label = "DTP", shape="roundedbox",
..            description="Todo |DTP|_"];
        
..         A -> B;
..         B -> C;
..         C -> D;
..         D -> E;
..         E -> F;

..     }

Authors
=======

Main authors of the **StatisKit** software suite are:

* `P. Fernique <pfernique@gmail.com>`_,
* `J. Peyhardi <jean.peyhardi@gmail.com>`_.

Contributors can be found in the respective software suite **GitHub** `repositories <http://github.com/StatisKit>`_.