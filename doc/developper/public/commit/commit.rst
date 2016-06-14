.. _contribute-commit:

Commit your modifications
=========================

.. warning::

    The commit of modifications with **Git** is quite different from **Subversion**.
    In particular, **Git** will not consider that your local :code:`<branchname>` branch differs from :code:`origin <branchname>` branch until you committed your modifications (see :numref:`workflow-state-commit`).
    
    .. _workflow-state-commit:
    
    .. figure:: commit.gif
        
        Effect of **Git** commits
        
        Until you committed your modifications (1.), **Git** will not consider that your local :code:`<branchname>` branch differs from :code:`origin <branchname>` remote branch.
        
        .. note::
        
            While :code:`master` and :code:`origin master` are still synchronized, it is assumed that some work from other developpers has been integrated into the :code:`upstream master`.
            There are therefore two different versions of :code:`master` branches at the end of this step.
            
        .. note::
        
            The commit of modifications do not implies the upload of these modifications.
            The branches :code:`<branchname>` and :code:`origin <branchname>` are therefore no more synchronized.

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


The **Git** Commit
------------------

Once the index is build as desired, it must be committed in order to make another snapshot of the repository.
This is done using the :code:`git commit` command.
If you leave off the :code:`-m` option, this command open your favorite editor (see :doc:`../configuration`) where you can construct a message associated to the commit.
Two commits are distinguished:

Backup & service commits
    These commits are not corresponding to particular development stages and can be used when uploading is a neccessity.
    For example these commits arise when a developper wants to:
    
    * Remotly save his developments.
    * Use a service (see :doc:`create`).

    For this type of commits, please use the :code:`git commit -m "<shortdesc>"` command where :code:`<shortdesc>` is a short summary of the commit.
    This summary should be less that 50 characters.

Developement commits
    The commits are all commits not considered as backup. 
    Please avoid the usage of the :code:`-m` option and produce a nice commit message using the follwing steps (the reader can refer to the `A Better Git Commit <https://web-design-weekly.com/2013/09/01/a-better-git-commit/>`_ message to more informations):

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

    .. code-block:: console
    
        git commit -a

    is used for automatically staged files that have been modified and deleted, but new files you have not told **Git** about are not affected.
    In this fact this command is different from the commands

    .. code-block:: console

        git add -A
        git commit

    that will also add new files.

.. note::

    Once this step is done, refers to the :ref:`workflow <contribute-workflow>` to continue.
