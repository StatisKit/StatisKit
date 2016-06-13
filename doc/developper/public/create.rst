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
..  File authors: Pierre Fernique <pfernique@gmail.com> (19)                        ..
..                                                                                  ..
.. ................................................................................ ..

Create a new repository
#######################

.. warning::
    
    Only owners of the **StatisKit** organization can create new repositories.
    
To create a new repository use the :code:`statiskit create` command.
This command launches the following workflow in order to create a new repository on the StatisKit organization.
To perform this, :code:`statiskit create` uses the **PyGithub** package to access `GitHub` interface in `Python`.
    
.. blockdiag::
    :align: center
    :desctable:
    
    blockdiag {

        A [label = "Initialize", shape="roundedbox",
           description="See `Initialize the repository`_ section. In order |br|
                        to enable code review from mainteners, the |br|
                        development must be short (i.e. one branch for one |br|
                        task such as new feature, bug fix...)."];
        B [label = "Complete", shape="roundedbox",
           description="See `Complete the repository`_ section. In order |br|
                        to benefit from tools developped by mainteners and |br|
                        ensure code quality, the development must respect |br|
                        some guidelines."];
        C [label = "Activate", shape="roundedbox",
           description="See `Activate repository services`_ section. Commits |br|
                        are snapshots of the repository. There are useful |br|
                        in particular for versionning software or create |br|
                        backups."];
        
        A -> B -> C;
    }

.. |br| raw:: html

   <br />
   
   
Initialize the repository
=========================

First of all, you need to specify which coding languages will be considered in this repository

.. code-block:: console

    $ statiskit create --languages <proglang-0> <proglang-1>
    
For instance, you can replace :code:`<proglang-0>` by :code:`cpp` and :code:`<proglang-1>` by :code:`py` to produce a repository that will host both `C++` and `Python` sources.

The initialization of a repository is made on GitHub (see this `page <https://help.github.com/articles/create-a-repo/>`_ for more details).
Your `gitHub` credentials (:code:`<username>` and :code:`<password>`) are therefore required:

.. code-block:: console

    Username for 'https://github.com': <username>
    Password for 'https://pfernique@github.com': <password>
    
Then, the :code:`statiskit create` will ask you most of informations that will be required if you had click on the |NEWBUTTON| of the the **StatisKit** `organization page <https://github.com/StatisKit>`_

.. code-block:: console

    Enter a repository name: <reponame>
    Enter a brief description: <repodesc>
    
This stage is equivalent to the filling of the following two fields:

* |REPOSITORYNAME| with a short, memorable and explicit name.
  For repositories that are concerning statistical methods, the name must begin with :code:`StatisKit-`.
  For instance :code:`StatisKit-Core` denote a repository that contains basic statistical classes and methods (dataframes, classical univariate and multivariate distributions or regressions) that will be used in repositories containing more complex statistical methodology (e.g. :code:`StatisKit-Tree`).
* |REPOSITORYDESC| with a short and explicit description of the repository purposes.
Once these both steps done, click on |CREATEBUTTON|.

.. warning::

    At this point:
    
    * Do not add a README (|READMEBOX|).
    * Do not select a :code:`.gitignore` file (|GITIGNOREMENU|). 
    * Do not select a license (|LICENSEMENU|).

.. |NEWBUTTON| image:: plus_new_repository_button.png
               :target: https://github.com/organizations/StatisKit/repositories/new
               :scale: 100%
               :alt: the new repository button

.. |REPOSITORYNAME| image:: repository_name.png
                    :scale: 100%
                    :alt: the repository name field

.. |CREATEBUTTON| image:: create_repository_button.png
                  :scale: 100%
                  :alt: the create repository button

.. |READMEBOX| image:: add_readme_box.png
               :scale: 100%
               :alt: the add readme box not checked

.. |GITIGNOREMENU| image:: add_gitignore_menu.png
                   :scale: 100%
                   :alt: the ignore menu set to :code:`None`

.. |LICENSEMENU| image:: add_license_menu.png
                 :scale: 100%
                 :alt: the license menu set to :code:`None`
                 
.. |REPOSITORYDESC| image:: repository_desc.png
                    :scale: 100%
                    :alt: the repository description field

Complete the repository
=======================

For now your repository is empty and you will need to complete it in order to respect **StatisKit** standards.
For instance, let consider that you initialized a repository denoted by :code:`<repository>`, then you must open a terminal and

1. Clone the **GitHub** repository
   
   .. code-block:: console
   
        git clone git@github.com:StatisKit/<repository>.git

2. Enter in local repository directory

   .. code-block:: console

        cd <repository>

3. Run the following shell :download:`script <repository.sh>`

   .. code-block:: console

        wget statiskit.readthedocs.io/en/latest/developper/public/repository.sh
        bash repository.sh

   This script requires the **MngIt** package and execute the following commands
   
   .. literalinclude:: repository.sh
      :language: bash
      :linenos:

4. Remove the local repository
   
   .. code-block:: console

        cd ..
        rm -rf <repository>


Activate repository services
============================


.. MngIt

.. |NAME| replace:: StatisKit

.. |BRIEF| replace:: meta-repository providing general documentation and tools for the **StatisKit** Organization

.. |VERSION| replace:: v0.1.0

.. |AUTHORSFILE| replace:: AUTHORS.rst

.. _AUTHORSFILE : AUTHORS.rst

.. |LICENSENAME| replace:: CeCILL-C

.. |LICENSEFILE| replace:: LICENSE.rst

.. _LICENSEFILE : LICENSE.rst

.. MngIt
