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
    * Install **Miniconda** if you are only interested by **StatisKit**.
    * Install **Conda** from :code:`.pkg` installer on **Mac Os X**.
    * Install **Miniconda 3** or **Anaconda 3** since the supported version of **Statiskit** is based on *Python 3*. 

.. _section-user-install-recommanded:

.. warning::

  From that point on, any command line should be typed 

  * For **Windows** users, in the **Anaconda Prompt** console that is available in the **Windows** start menu.
  * For **Unix** users, in your favorite **Terminal** configured to use **Conda**.
    To do so, for **Linux** users, it can be required to type the following command line

    .. code-block:: console

      echo ". <CONDA_PREFIX>/etc/profile.d/conda.sh" >> ~/.bashrc  

    where :code:`<CONDA_PREFIX>` must be replaced by the path where **Conda** has been installed.

Recommanded Installation
========================

The recommended installation rely on a **Conda** meta-package.
To install the *Python* interface, type the following command lines

.. code-block:: console

  conda create -n python-statiskit python-statiskit -c statiskit -c defaults --override-channels

Then, to activate the :code:`python-statiskit` environment, type the following command line

.. code-block:: console

  conda activate python-statiskit