To do so, type the following commands in your console

.. code-block:: console

   git pull
   git push

.. warning::

   Before using these commands, it is better to make sure that there are no uncommitted changes nor untracked files on your local repository.
   To do so, type the following command in your console

   .. code-block:: console

      git status

   If you want to suppress (permanently) all uncommitted changes, type the following command in your console

   .. code-block:: console

      git reset --hard

   Moreover; if you want to suppress (permanently) all untracked files, type the following command in your console

   .. code-block:: console
   
      git clean -fd