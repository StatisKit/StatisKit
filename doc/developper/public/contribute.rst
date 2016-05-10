Contribute to a repository
##########################

When using **Git** you should constently keep in mind the following warning:

.. warning::
    
    Never work on master, always on a branch

In order to contribute to an official repository of **StatisKit** we therefore recommand to follow the following workflow.
This workflow is assuming that you forked the official repository in your personal account and cloned it (see :doc:`fork`).

.. blockdiag::
    :align: center
    :desctable:
    
    blockdiag {

        A [label = "Branch", shape="roundedbox", description="See `Create a development branch`_ section. |br|
                                                              In order to enable code review from mainteners, the development must be short |br|
                                                              (i.e. one branch for one task such as new feature, bug fix...)."];
        B [label = "Work", shape="roundedbox", description="See `Work on your modifications`_ section. |br|
                                                            In order to benefit from tools developped by mainteners and ensure code quality, |br|
                                                            the development must respect some guidelines."];
        C [label = "Commit", shape="roundedbox", description="See `Commit your modifications`_ section."];
        D [label = "Upload ?", shape="diamond", description="If you want to upload your modifications to your personal repository, |br|
                                                             you shoud use the :code:`git push` command."];
        E [label = "Finished ?", shape="diamond", description="If your work on the branch is done, you should submit your modifications |br|
                                                               to the official repository."];
        F [label = "Submit", shape="roundedbox", description="See `Submit your modifications`_ section."];
        
        A -> B -> C;
        C -> D;
            
        D -> B;
        E -> B [label = "No"];

        group {
            orientation = portrait;
            color = "#FFFFFF";
            
            D -> E;
            E -> F;
        }
    }

.. |br| raw:: html

   <br />

Create a development branch
===========================

In order to create a development branch, you must first synchronize your :code:`master` local branch with the :code:`upstream master` remote branch.
This step ensure that you have all previously accepted modifications in the official repository.

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

.. code-block:: bash

    git push --set-upstream origin work_in_progress


.. note::

    Please choose an explicit name for your branch.


Work on your modifications
==========================

Commit your modifications
=========================

.. warning::

    The commit of modifications with **Git** is quite different from **Subversion**.

The *repository index*
----------------------

In **Git**, the *repository index* notion is primordial (see the this `post <http://www.gitguys.com/topics/whats-the-deal-with-the-git-index/>`_ for more details).
In short, files in the *repository index* are files that would be committed to the repository if you used the :code:`git commit` command.
However, files in the *repository index* are not committed to the repository until you use the :code:`git commit` command.
Therefore, in order to commit your modifications you must first build the *repository index* using file additions and removals.
For this step the :code:`git status`, :code:`git add` and :code:`git rm` commands are your friends:

:code:`git status`
    Tells you what files:

    * have been added to the *repository index*,
    * exists in the working tree but are not in the *repository index*,
    * have different contents between the working tree and the *repository index*.

:code:`git add <pathspec>`
    Add the :code:`<pathspec>` file to the repository index.
    
    .. warning::
    
        Contrarily to **Subversion**, with **Git** the :code:`git add` command must be performed not only for adding new files but also for modified files.
        By default no file is added in the index.
       
    For more details, refers to the **Git** manual (:code:`git add --help`).

:code:`git rm <pathspec>`
    Remove the :code:`<pathspec>` file from the working tree and the index.
    For more details, refers to the **Git** manual (:code:`git remove --help`).

    .. note::

        If you do not want to remove the  :code:`<pathspec>` file from you working tree but only in the *repository index* use :code:`git rm --cached <pathspec>` instead.

.. note::

    Since the incremental addition or removal of files can be tidious, the commands :code:`git add -A` can be of most interest.
    This command will also add files that were created.
    Therefore in order to add only relevant files, the :code:`.gitignore` file is of most importance (see :doc:`create`). 


Commit
------

Once 
Please write a good commit message and try to limit using the :code:`-m` flag.

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

.. note::

    If you want to add to your index deleted or modified files when committing, you can use the :code:`-a` flag.
    The command

    .. code-block:: bash
    
        git commit -a

    is used for automatically staged files that have been modified and deleted, but new files you have not told **Git** about are not affected.
    In this fact this command is different from the commands

    .. code-block:: bash

        git add -A
        git commit

    that will also add new files.

.. blockdiag::

   blockdiag {
       A [label = "Is the commit a save ?", shape="diamond"];
       B [label = ":code:`git commit -m 'A short message'", shape="roundedbox"];
       C [label = "Commit your\nmodifications", shape="roundedbox"];
       D [label = "Work\nfinished ?", shape="diamond"];
       E [label = "Submit your\nmodifications", shape="roundedbox"];

       A -> B -> C;
       C -> D;
       D -> B [label = "No"];
       D -> E [label = "Yes"];
   }


Submit your modifications
=========================
