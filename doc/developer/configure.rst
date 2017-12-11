.. _section-developer-configure:

Configure your Computer
#######################

In order to ease the development of the **StatisKit** software suite on multiple operating systems, the **Conda** package and environment management system is used.
To insall **Conda** refer to the section :ref:`section-user-install_it-prerequisites`.

Once **Conda** installed, you need to create the development environment called :code:`statiskit-dev` on your machine.
To do so you must:

* On Windows OSes, download and install **Visual Studio Community 2013** on this `page <https://www.visualstudio.com/vs/older-downloads/>`_ and,

  1. Install :code:`statiskit-dev` package in the :code:`statiskit-dev` environment.
  
     .. code-block:: console
  
        conda create -n statiskit-dev statiskit-dev -c statiskit

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

  2. Activate the created environment for each build of **Statiskit** software suite.

     .. code-block:: console

        activate statiskit-dev
          
* On Unix Oses, you can either:

  * Set your system configuration as the default **Travis CI** configuration (see this `page <https://docs.travis-ci.com/user/reference/osx/#OS-X-Version>`_ for OsX or install the version 5 of the :code:`gcc` compiler for Linux OSes) and,
    
    1. Install :code:`statiskit-dev` package in the :code:`statiskit-dev` environment.
  
       .. code-block:: console
  
          conda create -n statiskit-dev statiskit-dev -c statiskit
          
    3. Activate the created environment for each build of **Statiskit** software suite.

       .. code-block:: console

          source activate statiskit-dev
          
  * Build from sources as follows,
  
    1. Install :code:`conda-tools` package in the :code:`root` environment.

       .. code-block:: console

          conda install -n root conda-tools -c statiskit
          
       .. warning::
       
          You perhaps need to use the following commands to be able to use the :code:`conda release` command afterwards:
          
          .. code-block:: console
          
             source activate root
             $CONDA_PREFIX/bin/conda-release -h

    2. Clone the :code:`StatisKit` repository of the :code:`StatisKit` organization.

       .. code-block:: console

          git clone --recursive https://github.com/StatisKit/StatisKit.git

       .. note::

          If **git** is not installed on your computer, you can install it with conda

          .. code-block:: console

             conda install -n root git

    3. Enter the :code:`StatisKit` directory.
    
       .. code-block:: console
       
          cd StatisKit
          
    4. Build all **Conda** recipes available in this repository using :code:`conda-release`.

       .. code-block:: console
      
          conda realease . -c statiskit
         
       .. warning::
      
          **git** submodules can be out of date, to update all submodules proceed as follows
        
          .. code-block:: console
        
             git submodule update --recursive --remote

       .. note::

          If one build failed, you can re-use the previous commands.
          But, if you want to re-build successful builds, add the :code:`--no-inspect-conda-bld-directory` option.

    5. Install the :code:`statiskit-dev` package in an eponymous environment

       .. code-block:: console

          conda create -n statiskit-dev statiskit-dev --use-local

    6. Activate the created environment for each build of **Statiskit** software suite.

       .. code-block:: console

          source activate statiskit-dev
