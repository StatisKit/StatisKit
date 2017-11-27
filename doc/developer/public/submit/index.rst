.. _contribute-submit:


Submit your modifications
=========================

Prepare your pull-request
-------------------------

.. _workflow-pull-prepare-state:

.. figure:: prepare.gif
    :alt: Create a development branch
    
    Steps of the development branch creation.
    
    Repositories of the same color are synchronized.

    
Before submitting your modifications, you must recover changes from :code:`upstream master` remote branch in your local :code:`master` branch

.. code-block:: console

        git checkout master
        git pull upstream master

and upload the changes in your :code:`origin master` remote branch

.. code-block:: console

        git push

.. Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ..
..                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
.. Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
..                                                                       ..
.. This file is part of the StatisKit project. More information can be   ..
.. found at                                                              ..
..                                                                       ..
..     http://statiskit.rtfd.io                                          ..
..                                                                       ..
.. The Apache Software Foundation (ASF) licenses this file to you under  ..
.. the Apache License, Version 2.0 (the "License"); you may not use this ..
.. file except in compliance with the License. You should have received  ..
.. a copy of the Apache License, Version 2.0 along with this file; see   ..
.. the file LICENSE. If not, you may obtain a copy of the License at     ..
..                                                                       ..
..     http://www.apache.org/licenses/LICENSE-2.0                        ..
..                                                                       ..
.. Unless required by applicable law or agreed to in writing, software   ..
.. distributed under the License is distributed on an "AS IS" BASIS,     ..
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or       ..
.. mplied. See the License for the specific language governing           ..
.. permissions and limitations under the License.                        ..

Then, you must rebase your local development branch with your local :code:`master` branch.

.. code-block:: console

        git checkout <branchname>
        git rebase master

If conflicts occur, fix conflicts for each file and finish rebase

.. code-block:: console

        git rebase --continue

.. note::

    Any file modified when fixing conflicts should be added using the :code:`git add <pathspec>` command.

If anything has gone wrong, you can abort reabase

.. code-block:: console

        git rebase --abort

Create your pull-request
------------------------

.. _workflow-pull-propose-state:

.. figure:: propose.gif
    :alt: Create a development branch
    
    Steps of the development branch creation.
    
    Repositories of the same color are synchronized
    
On github interface, select your branch :code:`<branchname>` and click on pull-request (see this `post <https://help.github.com/articles/using-pull-requests/>`_ for more details).

.. warning::

    You must see the following message: "Able to merge. These branches can be automatically merged".
    If it's not the case, the :code:`upstream master` has probably diverged.
    You must therefore turn back to previous step (see `Prepare your pull-request`_ section).

If all steps described in the workflow are respected, your branch is clean and mainteners have absolutely nothing to do to integrate your work (except to review your changes) and so it will certainly be integrated.

Integrate your pull-request
---------------------------

.. _workflow-pull-integrate-state:

.. figure:: integrate.gif
    :alt: Create a development branch
    
    Steps of the development branch creation.
    
    Repositories of the same color are synchronized
    
.. note::

    Once your branch is integrated in the :code:`upstream master`, it is recommanded to to delete your branch:

    * On your local repository,

      .. code-block:: console
      
            git checkout master
            git branch -d <branchname>

    * On your personal repository,

      .. code-block:: console
      
            git push origin --delete <branchname>

.. warning::

    Once this step is done, refers to the :ref:`workflow <contribute-workflow>` to continue.
