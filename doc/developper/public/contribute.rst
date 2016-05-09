Contribute to a repository
##########################

In the following we assume that you previously forked the official repository to your personal account.
If not, go to the GitHub help page concerning `repository forking <https://help.github.com/articles/fork-a-repo>`_.

.. note::

    According to this documentation, the :code:`upstream master` remote branch refers to the master branch of the repository on the *StatisKit* organization account and :code:`origin master` remote branch to the repository fork on your personal account.


.. blockdiag::

   blockdiag {
       A [label = "Create a development branch", shape="roundedbox"];
       B [label = "Work on your\nmodifications", shape="roundedbox"];
       C [label = "Commit your\nmodifications", shape="roundedbox"];
       D [label = "Work\nfinished ?", shape="diamond"];
       E [label = "Submit your\nmodifications", shape="roundedbox"];

       A -> B -> C;
       C -> D;
       D -> B [label = "No"];
       D -> E [label = "Yes"];
   }

Create a development branch
===========================

.. warning::
    
    Never work on master, always on a branch

In order to create a development branch, you must first synchronize your :code:`master` local branch with the :code:`upstream master` remote branch (This step ensure that you have all previously accepted modifications in the official repository).

.. code-block:: bash

    git checkout master
    git pull upstream master

Then, you must push modifications to your :code:`origin master` remote branch

.. code-block:: bash

    git push

Since all your master branches are up to date, you can create your local branch

.. code-block:: bash

    git checkout -b work_in_progress

and push it to your personal repository

.. code-block::

    git push --set-upstream work_in_progress

.. note::

    In order to enable code review from mainteners, the development must be short (i.e. one branch for one task sucha as new feature, bug fix...).

.. note::

    Please choose an explicit name for your branch.


Work on your modifications
==========================

Commit your modifications
=========================

In order to commit your modifications you must first precise which files to add, remove or modify in the remote **Git** repository.
Stores the current contents of the index in a new commit along with a log message from the user describing the changes.
For this step the :code:`git status`, :code:`git add` and :code:`git remove` commands are your friends:

:code:`git status`
    Give a

:code:`git add`
    Incrementally "add" changes to the index before using the commit command 
    
    .. warning::
    
        Contrarily to subversion, the :code:`git add` command must be performed not only for adding new files.
        Even modified files must be "added".
        
        .. note::
        
            :code:`git add -A`

:code:`git remove`
    Remove files from the working tree and the index, again before using the commit command;


Please write a good commit message and try to limit using the `-m` commit flag.

Using

.. code-block:: bash
    
    git commit

should open your favorite editor (see :doc:`configure`) where you can construct a better commit by following some of these simple steps (the reader can refer to the `A Better Git Commit <https://web-design-weekly.com/2013/09/01/a-better-git-commit/>`_ message to more informations):

* The first line should be a short summary.
  Referencing the bug number or the main accomplishment of the change (e.g “Fixes issue #8976″).
  This is the title of your commit and should be less than 50 characters.

* Then a line break.

* Followed by a longer detailed description about the things that changed.
  This section is a really good place to explain what and why.
  You could cover statistics, performance wins, roadblocks, etc. The text should be wrapped at 72 characters.

Submit your modifications
=========================
