Fork and/or clone a repository
##############################

To fork and/or clone a repository of the **StatisKit** organization, we recommend to use the :code:`statiskit clone` command.
To perform these steps, :code:`statiskit clone` uses the PyGithub package to access `GitHub` interface in `Python`.
Your gitHub credentials (<username> and <password>) are therefore required .

.. code-block:: console

    $ statiskit clone
    Username for 'https://github.com': <username>
    Password for 'https://pfernique@github.com': <password>
    
Let us consider a repository identified by :code:`<reponame>`

.. code-block:: console

    Enter a repository name: <reponame>
    
This command:

1. Fork the :code:`<reponame>` into your account.

   .. warning::
   
        The :code:`<reponame>` must exists in the **StatisKit** organization.

   .. note::

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

        If you already forked the :code:`<reponame>` it will not be forked one more time.

2. Clone it on your disk at your current location within the :code:`<reponame>` directory.

   .. warning::

        If your fork of the :code:`<reponame>` repository is not named :code:`<reponame>`, Its name will be used in place of :code:`<reponame>` for the directory that contains the clone.
        
    
   .. note::
    
        By default, the clone is performed using SSH remote url. 
        If you prefer to use the HTTPS remote url, use the :code:`url` argument of the :code:`statiskit clone` command:
        
        .. code-block:: console
        
            $ statiskit clone --url=https
        
3. Add the :code:`upstream` remote that refers to the repository on the **StatisKit** organization.
   
   .. note::
   
        By default, the :code:`origin` remote refers to the repository on your account.
    
    
.. figure:: clone.png
    :alt: Repository status after fork and clone steps.

    Repository status after fork and clone of a repository. 
    
    The repository is named :code:`<reponame>`.
    The left hand cloud represents the repository on the **StatisKit** organization `GitHub` account. 
    The right hand clound represents the forked repository on your :code:`<username>` `GitHub` account.
    The computer represents the cloned repository on your computer.
    
    .. note::
    
        Cloning a repository using **Git** only adds the :code:`origin` remote.
        The principale value added of the :code:`statiskit clone` command is to add the :code:`upstream` remote.
        For example, this enable you to compare your local branch to both remote branches using:
    
        * for the remote branch on the **StatisKit** `GitHub` account,
    
          .. code-block:: console
    
                $ git diff upstream/master 
        
        * for the remote branch on your :code:`<username>` `GitHub` account,
    
          .. code-block:: console
    
                $ git diff origin/master
        
          Or, since :code:`origin` is chosen by default,
      
          .. code-block:: console
    
                $ git diff master