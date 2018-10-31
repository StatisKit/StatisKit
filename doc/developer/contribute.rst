.. _section-developer-contribute:

Contribute to a Repository
##########################

.. warning::

    It is here assumed the :code:`statiskit` environment has been installed and activated as detailed in the :ref:`section-developer-configure` section.

.. note::

    This section heavily relies on the **devops-tools** program.
    For more information concerning the :code:`github`, :code:`travis_ci` and :code:`appveyor_ci` commands, refer to their `documentation <http://devops-tools.rtfd.io>`_.

Official repositories of **StatisKit** are currently hosted on GitHub.
In order to contribute to an official repository of **StatisKit** we recommend to proceed as follows.

.. note::

   In the following :code:`<REPOSITORY>` denote the official repository name.

1. Fork the repository from the organization account to your personal account.
   If this repository is already forked on your personal account, you can skip this step.
   Otherwise, type the following command in your console

   .. code-block:: console

      github fork <REPOSITORY> --owner=StatisKit

2. Clone the repository from your personal account to your computer.
   If this repository is already cloned on your computer, you can skip this step.
   Otherwise, type the following command in your console

   .. code-block:: console

      github clone <REPOSITORY>

   .. warning::

      After this step, it is assumed that your console working directory is the one of the local repository.
      Two remotes are available for this local repository:

      * The :code:`upstream` remote pointing to the repository located on the organization account.
      * The :code:`origin` remote pointing to the repository located on your personal account.

3. Activate Continuous Integration and Deployment (CI&D) services for the repository located on your personal account.
   This step is not mandatory but is recommended.
   To do so, type the following commands in your console

   .. code-block:: console

      travis_ci init --anaconda-label=main
      appveyor_ci init --anaconda-label=main

   .. warning::

      To activate CI&D services, you need to have:

      * A Travis CI `account <https://travis-ci.org>`_.
      * A AppVeyor CI `account <https://ci.appveyor.com>`_.

3. Retrieve the latest code from the repository located on the organization account and push it together with your modifications to the repository located on your personal account.
   This step is particularly important if you skipped one of the first two.

   .. include:: sync.rst

4. Work on your local repository.
   To work on a repository, an issue must first have been published.

   .. warning::

      Issues must be published on the repository located on the organization account, not on your personal repository.

   To search for existing issues or creating new ones using your Web browser, type the following command

   .. code-block:: console

      github issues --browser

   To display in your console current open issues, type the following command in your console

   .. code-block:: console

      github issues

   To display in your console current open issues that are assigned to yourself (i.e., that you are currently working on), type the following command in your console

   .. code-block:: console

      github issues --assigned

   In the following, we consider that an issue is identified by its number denoted by :code:`<ISSUE>`.
   If this issue corresponds to:

   * a bug, the work must typically be situated on a branch named :code:`hotfix_<ISSUE>` created from the :code:`master` branch of the repository located on the organization account.
     Thus, type the following command in your console
   
     .. code-block:: console

        github hotfix --issue=<ISSUE>

     Yet, if you do not have the necessary permissions to write on the repository located on the organization account, the branch must be created from the :code:`master` branch of your personal account.
     To do so, type the following command in your console
   
     .. code-block:: console

        github hotfix --issue=<ISSUE> --remote=origin

   * an enhancement, the work must typically be situated on a branch named :code:`feature_<ISSUE>` created from the :code:`master` branch of the repository located on your personal account.
     Thus, type the following command in your console

     .. code-block:: console

        github feature --issue=<ISSUE>

     If the enhancement should be assigned to more than one developer (large ones), the branch must be create from the :code:`master` branch of the organization repository.
     To do so, type the following command in your console

     .. code-block:: console

        github feature --issue=<ISSUE> --remote=upstream

   .. note::

      If the bug or the feature covers more than one issue, create a new issue referencing all those issues.
      In all those issues:

      * add the :code:`Duplicate of #<ISSUE>` comment,
      * add the :code:`duplicate` label.

   .. warning::

      If the branch name given by the `github hotfix` or `github fixture` commands corresponds to a remote branch, the remote will be set to the existing remote branch. 

   For more information concerning how to amend a repository, refer to the :ref:`section-developer-FAQ` section.
   If this step has already been made once on your local repository, type one the following commands in your console

   .. code-block:: console

      github start hotfix_<ISSUE>

   or

   .. code-block:: console

      github start feature_<ISSUE>

   To see all available branches of your local repository, type the following command in your console

   .. code-block:: console

      git branch

   To see all available branches of all repositories, type the following command in your console 

   .. code-block:: console

      git branch -a

   An easiest way if you have no concurrent branches is to use the following command line

   .. code-block:: console

      github start

   This command will ensure that you are currently working on the latest branch you edited using these commands.

   .. warning::

      If there are untracked files or uncommitted changes on your current local branch, this command will fail.

   Similarly, to go back to the local :code:`master` branch, type the following command

   .. code-block:: console

      github end

   .. warning::

      If there are untracked files or uncommitted changes on your current local branch, this command will fail.

   .. note::

      At any point, to seek information about a particular issue using your Web browser, type the following command in your console

      .. code-block:: console

         github issue <ISSUE> --browser

      If you are currently working on a branch and want to seek information about the corresponding issue using your Web browser, type the following command in your console

      .. code-block:: console

         github issue --browser

      This is particularly helpful if you forgot the meaning of an issue number you were working on.

5. Retrieve the latest code from the repository located on the organization account and push it together with your modifications to the repository located on your personal account.

   .. include:: sync.rst

6. Suggest to maintainers to incorporate your modifications into the :code:`master` branch of the repository located on the organization account.
   To do so, type the following command in your console

   .. code-block:: console

      github end --suggest

   .. warning::

      If your local branch is at least one commit behind the :code:`master` branch of the repository located on the organization account or is ahead of the corresponding branch on the repository location on your personal account, this command will fail.