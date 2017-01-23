.. _create_initialize:

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
