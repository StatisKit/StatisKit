.. Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ..
..                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
.. Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
..                                                                       ..
.. This file is part of the StatisKit project. More information can be   ..
.. found at                                                              ..
..                                                                       ..
..     http://statiskit.rtfd.io                                          ..
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

.. _section-user-install:

Install it !
############

.. _section-user-install-prerequisites:

Prerequisites
=============

In order to ease the installation of the **StatisKit** software suite on multiple operating systems, the **Conda** package and environment management system is used.

.. note::

    For more information refers to the **Conda** `documentation <http://conda.pydata.org/docs>`_.

To install **Conda**, please refers to this `page <https://conda.io/docs/user-guide/install/index.html>`_.
Installers for:

* **Miniconda** are available on this `page <https://conda.io/miniconda.html>`_.
* **Anaconda** are available on this `page <https://www.anaconda.com/download/>`_.

.. note::

    We recommend to:
    
    * Follow the instructions given for the regular installation.
    * Pay attention to the :code:`PATH` environment variable.
    * Install **Miniconda** if you are only interested by **Statiskit**.
    * Install **Miniconda 3** or **Anaconda 3** since the supported version of **Statiskit** is based on *Python 3*. 

.. warning::

    In the following, it is assumed that the **Conda** :code:`activate` scripts are available from the command line (see the :code:`PATH` environment variable).

.. _section-user-install-recommanded:

Recommanded Installations
=========================

The recommended installations rely on **Conda** meta-packages.
Choose an interface and proceed as detailed in the corresponding section:

.. toctree::
    :maxdepth: 1

    API/cpp
    API/python
