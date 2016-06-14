Create a development branch
===========================

.. note::

    Please choose an explicit name for your branch.
    
    
.. figure:: branch.gif
    :alt: Create a development branch
    
    Steps of the development branch creation.
    
    Repositories of the same color are synchronized.
    Before the creation of your development branch, all three repositories are not synchronized.
    In:
    
    1. Your local :code:`master` branch is synchronized with the :code:`upstream master` branch.
    
       .. code-block:: console
       
            git checkout master
            git pull upstream master
    
    2. Your remote :code:`origin master` branch is synchronized with your local :code:`master` branch.
 
       .. code-block:: console
       
           git push

    3. Since all your master branches are synchronized, the local :code:`<branchname>` branch is created
    
       .. code-block:: console
       
            git checkout -b <branchname>

    4. Then, the remote  :code:`origin <branchname>` branch is created in order to enable the uploading of future modifications into your :code:`<username>` `GitHub` account.

       .. code-block:: console

            git push --set-upstream origin <branchname>

.. warning::

    Once this step is done, refers to the :ref:`workflow <contribute-workflow>` to continue.
