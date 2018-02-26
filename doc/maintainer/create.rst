.. _section-maintainer-create:

Create a new repository
#######################

.. warning::

    It is here assumed the:code:`statiskit-dev` environment has been installed and activated as written in Section :ref:`section-developer-configure`.
    This section heavily relies on the **devops-tools** program.
    For more information on the :code:`github`, :code:`travis_ci` and :code:`appveyor_ci` commands, refer to their `documentation <http://devops-tools.rtfd.io>`.
    
Official repositories of **StatisKit** are currently hosted on GitHub.
In order to create an official repository of **StatisKit** we recommend to proceed as follows.

.. note::

   In the following :code:`<REPOSITORY>` denote the official repository name.

1. Initialize the repository on the organization account.
   To do so, type the following command in your console

   .. code-block:: console

      github init <REPOSITORY> --owner=StatisKit --license=apache-2.0

2. Clone the repository from the organization account to your computer.
   If this repository is already cloned on your computer, you can skip this step.
   Otherwise, type the following command in your console

   .. code-block:: console

      github clone <REPOSITORY> --owner=StatisKit

   .. warning::

      After this step, it is assumed that your console working directory is the one of the local repository.

3. Activate Continuous Integration and Deployment services for your repository.
   Contrarily to user repositories, this step is mandatory for organization account's repositories.
   To do so, type the following commands in your console

   .. code-block:: console

      travis_ci init --anaconda-label=develop
      appveyor_ci init --anaconda-label=develop

3. Populate the repository with relevant files.

   .. warning::

      Until now, the repository structure has not been clearly set.
      More information can be gathered in the :ref:`section-developer-FAQ` section.
      A package is yet under consideration to propose command lines to simplify the process (e.g., :code:`layout init`).

4. Retrieve the latest code from the repository located on the organization account and push your modifications to the repository located on the organization account.

   .. code-block:: console

      github flow sync
      
.. note::

  For more information concerning naming conventions and places for files specific to further repository developments, refer to the :ref:`section-developer-FAQ` section.