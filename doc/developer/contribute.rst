.. _section-developer-contribute:

Contribute to a repository
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

3. Activate Continuous Integration and Deployment services for the repository located on your personal account.
   This step is not mandatory but is recommended.
   To do so, type the following commands in your console

   .. code-block:: console

      travis_ci init --anaconda-label=main
      appveyor_ci init --anaconda-label=main

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

      github issues --only-me

   In the following, we consider that an issue is identified by its number denoted by :code:`<ISSUENUMBER>`.
   If this issue corresponds to:

   * a bug, the work must typically be situated on a branch named :code:`hotfix_<ISSUENUMBER>` created from the :code:`master` branch of the repository located on the organization account.
     Thus, type the following command in your console
   
     .. code-block:: console

        github hotfix <ISSUENUMBER>

   * a feature, the work must typically be situated on a branch named :code:`feature_<ISSUENUMBER>` created from the :code:`master` branch of the repository located on your personal account.
     Thus, type the following command in your console

     .. code-block:: console

        github feature <ISSUENUMBER>

     If the feature should be assigned to more than one developer, type instead the following command in your console

     .. code-block:: console

        github feature <ISSUENUMBER> --shared

     This command will create a branch named :code:`feature_<ISSUENUMBER>` from the :code:`master` branch of the repository located on the organization account instead of your personal account in order to share more efficiently developers' modifications.

   .. note::

      If the bug or the feature covers more than one issue, create a new issue referencing all those issues.

   For more information concerning how to amend a repository, refer to the :ref:`section-developer-FAQ` section.
   If this step has already been made once on your local repository, type the following command in your console

   .. code-block:: console

      github start <ISSUENUMBER>

   An easiest way if you have no concurrent branches is to use the following command line

   .. code-block:: console

      github start

   This command will ensure that you are currently working on the latest branch edited.
   Similarly, to go back to the local :code:`master` branch, type the following command

   .. code-block:: console

      github end

   .. note::

      At any point, to seek information about a particular issue using your Web browser, type the following command in your console

      .. code-block:: console

         github issue <ISSUENUMBER>

      If you are currently working on a branch and want to seek information about the corresponding issue, type the following command in your console

      .. code-block:: console

         github issue <ISSUENUMBER>

      This is particularly helpful if you forgot the meaning of an issue number you were working on.

5. Retrieve the latest code from the repository located on the organization account and push it together with your modifications to the repository located on your personal account.

   .. include:: sync.rst

6. Suggest to maintainers to incorporate your modifications into the :code:`master` branch of the repository located on the organization account.
   To do so, type the following command in your console

   .. code-block:: console

      github flow end --suggest