.. _section-developer-contribute:

Contribute to a repository
##########################

.. warning::

    It is here assumed the:code:`statiskit-dev` environment has been installed and activated as written in Section :ref:`section-developer-configure`.
    This section heavily relies on the **devops-tools** program.
    For more information on the :code:`github`, :code:`travis_ci` and :code:`appveyor_ci` commands, refer to their `documentation <http://devops-tools.rtfd.io>`.

Official repositories of **StatisKit** are currently hosted on GitHub.
In order to contribute to an official repository of **StatisKit** we recommend to proceed as follows.

.. note::

   In the following :code:`<REPOSITORY>` denote the official repository name.

1. Fork the repository from the organization account to your personal GitHub account.
   If this repository is already forked on your GitHub account, you can skip this step.
   Otherwise, type the following command in your console

   .. code-block:: console

      github fork <REPOSITORY> --owner=StatisKit

2. Clone the repository from your personal GitHub account to your computer.
   If this repository is already cloned on your computer, you can skip this step.
   Otherwise, type the following command in your console

   .. code-block:: console

      github clone <REPOSITORY>

   .. warning::

      After this step, it is assumed that your console working directory is the one of the local repository.
      Two remotes are available for this local repository:

      * The :code:`upstream` remote pointing to the repository located on the organization account.
      * The :code:`origin` remote pointing to the repository located on your personal account.

3. Activate Continuous Integration and Deployment services for your repository.
   This step is not mandatory but is recommended.
   To do so, type the following commands in your console

   .. code-block:: console

      travis_ci init --anaconda-label=main
      appveyor_ci init --anaconda-label=main

3. Retrieve the latest code from the repository located on the organization account and push it together with your modifications to the repository located on your personal account.
   This step is particularly important if you skipped one of the first two.
   To do so, type the following command in your console

   .. code-block:: console

      github flow sync

   .. warning::

      This command will fail if any there is any uncommitted change.
      If you want to suppress (permanently) any uncommitted change, type the following command line

      .. code-block:: console

         git reset --hard
         git clean -fd

4. Work on the repository.
   To work on a repository, an issue must first have been published.

   .. warning::

      Issues must be created on the official repository, not your repository.

   To search for existing issues or creating new ones using your Web browser, type the following command

   .. code-block:: console

      github flow issues

   In the following, we consider that an issue is identified by its number denoted by :code:`<ISSUENUMBER>`.
   If this issue corresponds to:

   * a bug, the work must typically be situated on a branch named :code:`hotfix_<ISSUENUMBER>` created from the :code:`master` branch of the repository located on the organization account.
     Thus, type the following command in your console
   
   .. code-block:: console

      github flow hotfix start <ISSUENUMBER>

   * a feature, the work must typically be situated on a branch named :code:`feature_<ISSUENUMBER>` created from the :code:`master` branch of the repository located on your personal account.
     Thus, type the following command in your console

   .. code-block:: console

      github flow feature start <ISSUENUMBER>

   .. note::

      If the bug or the feature covers more than one issue, create a new issue referencing all those issues.

   For more information concerning how to amend a repository, refer to the :ref:`section-developer-FAQ` section.
   If this step has already been made once, the corresponding commands will ensure that you are currently working on the correct branch.
   An easiest way if you have no concurrent branches is to use the following command line

   .. code-block:: console

      github flow start

   that will ensure that you are currently working on the latest branch edited.
   Similarly, to go back to the local :code:`master` branch, type the following command

   .. code-block:: console

      github flow end

   .. note::

      To see all branches available, use the following command lines

      .. code-block:: console

         github flow sync --ignore-commits
         git branch -a

      To search for information about an existing issue using your Web browser, type the following command

      .. code-block:: console

         github flow issue <ISSUENUMBER>

      This is particularly helpful if you forgot the meaning of an issue number you were working on.

5. Retrieve the latest code from the repository located on the organization account and push it together with your modifications to the repository located on your personal account.
   To do so, type the following command in your console

   .. code-block:: console

      github flow sync

   .. warning::

      This command will fail if any there is any uncommitted change.
      If you want to suppress (permanently) any uncommitted change, type the following command line

      .. code-block:: console

         git reset --hard
         git clean -fd

6. Suggest to maintainers to incorporate your modifications into the :code:`master` branch of the repository located on the organization account.
   To do so, type the following command in your console

   .. code-block:: console

      github flow end --suggest