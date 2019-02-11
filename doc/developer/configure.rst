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

Once **Conda** is installed, you need to create a development environment called :code:`statiskit-toolchain` containing the meta-package :code:`statiskit-toolchain` on your computer.
To do so, type the following command line
  
.. code-block:: console

   conda create -n statiskit-toolchain statiskit-toolchain -c statiskit -c defaults --override-channels

Moreover, for

* **Windows** users, you must download and install **Visual Studio Community 2017** (available on this `page <https://visualstudio.microsoft.com/downloads/>`_).
* **Mac Os X** users, you must download and install **macOS 10.9 SDK**.
  This can be done using the following command lines

  .. code-block:: console

    git clone https://github.com/phracker/MacOSX-SDKs.git --depth=1
    sudo cp -r MacOSX-SDKs/MacOSX10.9.sdk /opt/MacOSX10.9.sdk
    rm -rf MacOSX-SDKs

.. Then, you need to download this :code:`conda_build_config.yaml` `file <https://raw.githubusercontent.com/StatisKit/travis-ci/master/conda_build_config.yaml>`_ and put in your home folder.
.. To do so, 

.. * **Windows** users should type the following command lines.

..   .. code-block:: console
    
..     curl https://raw.githubusercontent.com/StatisKit/travis-ci/master/conda_build_config.yaml -o %USERPROFILE%\conda_build_config.yaml

.. * **Unix** users should type the following command lines

..   .. code-block:: console
    
..     curl https://raw.githubusercontent.com/StatisKit/travis-ci/master/conda_build_config.yaml -o ${HOME}\conda_build_config.yaml

.. For conveniance, you can put this file into another directory.
.. To do so, move it manually and update your conda configuration file accordingly.
.. For more information, refer to this `page <https://docs.conda.io/projects/conda-build/en/latest/source/variants.html?highlight=variants#creating-conda-build-variant-config-files>`_.

.. warning::

  From that point on, any command line should be typed from the :code:`statiskit-toolchain` environment.
  To do so, type the following command lines each time you launch a new console

  .. code-block:: console

    conda activate statiskit-toolchain