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
           description="See `Initialize the repository`_ section. The repository |br|
                        initialization create an empty repository in the **StatisKit** |br|
                        organization."];
        B [label = "Complete", shape="roundedbox",
           description="See `Complete the repository`_ section. In order to complete |br|
                        the empty repository, you must respect some guidelines |br|
                        concering repository structures and mandatory files."];
        C [label = "Activate", shape="roundedbox",
           description="See `Activate repository services`_ section. In order to enable |br|
                        code review from mainteners, some web-services must be |br|
                        activated."];
        
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
    
    
Then, the :code:`statiskit create` will ask you 2 informations that are required to create the package

.. code-block:: console

    Enter a repository name: <reponame>
    Enter a brief description: <repodesc>
    
Normally, on `GitHub`, to create a new repository for the **StatisKit** `organization <https://github.com/StatisKit>`_, you need to click on the |NEWBUTTON|.
This stage is equivalent to the filling the following two fields on the page:

* |REPOSITORYNAME|, identified by :code:`<reponame>`, with a short, memorable and explicit name.
  For repositories that are concerning statistical methods, the name must begin with :code:`StatisKit-`.
  For instance :code:`StatisKit-Core` denote a repository that contains basic statistical classes and methods (dataframes, classical univariate and multivariate distributions or regressions) that will be used in repositories containing more complex statistical methodology (e.g. :code:`StatisKit-Tree`).
* |REPOSITORYDESC|, identified by :code:`<repodesc>`, with a short and explicit description of the repository purposes.

.. warning::

    At this point, if you use directly the `GitHub` interface (not recommended):
    
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

For now your repository is created but empty.
You need to complete it in order to respect **StatisKit** standards.
If you used the :code:`statiskit create` command this will be done automatically.
To commit changes and push them into the remote repository you must enter a short commit message :code:`<msg>`.

.. code-block:: console

    Enter a brief commit message: <msg>
    
If no commit message is given, the default commit message :code:`Initialize and complete the repository` is used.

.. todo::

    Add more informations about repository structure

Activate repository services
============================

If you look at the :code:`README.rst` file of the created repository, some web-services must be activated in order to obtain to respect **StatisKit** standards.
These services are:

* **Travis CI**.
  This `service <https://docs.travis-ci.com/>`_ is used to perform continuous integration of repositories.
* **Coveralls**.
  This `service <https://coveralls.zendesk.com/hc/en-us>`_ is used to show which parts of your code aren't covered by repository test suites.
* **Landscape**.
  This `service <https://docs.landscape.io/index.html>`_ is used to perform static analysis of your code within repositories.
* **Read The Docs**.
  This `service <http://docs.readthedocs.io/en/latest/>`_ is used to ensure that documentation of your code is uploaded to repository documentation websites.
  
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
