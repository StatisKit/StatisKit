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

.. _section-developer-configure:

Configure your Computer
#######################

In order to ease the development of the **StatisKit** software suite on multiple operating systems, the **Conda** package and environment management system is used.
To install **Conda** refer to the section :ref:`section-user-install-prerequisites`.

Once **Conda** is installed, you need to create a development environment called :code:`statiskit` containing the meta-package :code:`statiskit` on your computer.
To do so, type the following command line in your console
  
.. code-block:: console

   conda create -n statiskit statiskit -c statiskit/label/develop -c statiskit -c defaults --override-channels

.. warning::

   On Windows OSes you must first download and install **Visual Studio Community 2013** (available on this `page <https://www.visualstudio.com/vs/older-downloads/>`_).

Then, you can activate the created environment for each build of **StatisKit** software suite components by following instructions given after the installation.

.. note::

   If you want a fine grained configuration, report to the :ref:`section-developer-faq` section.