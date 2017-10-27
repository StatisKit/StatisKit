.. _section-developer-configure:

Configure your Computer
#######################

In order to ease the development of the **StatisKit** software suite on multiple operating systems, the **Conda** package and environment management system is used.
To insall **Conda** refer to the section :ref:`section-user-install_it-prerequisites`.

Once **Conda** installed, you need to create the development environment called :code:`statiskit-dev` on your machine.
To do so you must:

* On Windows OSes, install `Visual Studio Community 2013 <https://www.visualstudio.com/en-us/news/releasenotes/vs2013-community-vs>`_ and,

  1. Install :code:`statiskit-dev` package in the :code:`statiskit-dev` environment.
  
     .. code-block:: console
  
        conda install -n statiskit-dev statiskit-dev -c statiskit
          
  2. Activate the created environment for each build of **Statiskit** software suite.

     .. code-block:: console

        activate statiskit-dev
          
* On Unix Oses, you can either:

  * Set your system configuration as the default **Travis CI** configuration (see this `page <https://docs.travis-ci.com/user/reference/osx/#OS-X-Version>`_ for OsX or install the version 5 of the :code:`gcc` compiler for Linux OSes) and,
    
    1. Install :code:`statiskit-dev` package in the :code:`statiskit-dev` environment.
  
       .. code-block:: console
  
          conda install -n statiskit-dev statiskit-toolchain -c statiskit
          
    3. Activate the created environment for each build of **Statiskit** software suite.

       .. code-block:: console

          source activate statiskit-dev
          
  * Build from sources as follows,
  
    1. Install :code:`conda-tools` package in the :code:`root` environment.

       .. code-block:: console

          conda install -n root conda-tools -c statiskit

    2. Clone the :code:`StatisKit` repository of the :code:`StatisKit` organization.

       .. code-block:: console

          git clone --recursive https://github.com/StatisKit/StatisKit.git

       .. note::

          If **git** is not installed on your computer, you can install it with conda

          .. code-block:: console

             conda install -n root git -c conda-forge

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

          conda install -n statiskit-dev statiskit-dev --use-local -c statiskit

    6. Activate the created environment for each build of **Statiskit** software suite.

       .. code-block:: console

          source activate statiskit-dev
