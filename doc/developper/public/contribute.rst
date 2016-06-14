.. ................................................................................ ..
..                                                                                  ..
..  StatisKit: meta-repository providing general documentation and tools for the    ..
..  **StatisKit** Organization                                                      ..
..                                                                                  ..
..  Copyright (c) 2016 Pierre Fernique                                              ..
..                                                                                  ..
..  This software is distributed under the CeCILL-C license. You should have        ..
..  received a copy of the legalcode along with this work. If not, see              ..
..  <http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html>.                  ..
..                                                                                  ..
..  File authors: Pierre Fernique <pfernique@gmail.com> (26)                        ..
..                                                                                  ..
.. ................................................................................ ..

Contribute to a repository
##########################

When using **Git** you should constently keep in mind the following warning:

.. warning::
    
    Never work on master, always on a branch

In order to contribute to an official repository of **StatisKit** we therefore recommand to follow the following workflow.

.. _contribute-workflow:

.. blockdiag::
    :align: center
    :desctable:
    
    blockdiag {

        A [label = "Branch", shape="roundedbox",
           description="See `Create a development branch`_ section. In order |br|
                        to enable code review from mainteners, the |br|
                        development must be short (i.e. one branch for one |br|
                        task such as new feature, bug fix...)."];
        B [label = "Work", shape="roundedbox",
           description="See `Work on your modifications`_ section. In order |br|
                        to benefit from tools developped by mainteners and |br|
                        ensure code quality, the development must respect |br|
                        some guidelines."];
        C [label = "Commit", shape="roundedbox",
           description="See `Commit your modifications`_ section. Commits |br|
                        are snapshots of the repository. There are useful |br|
                        in particular for versionning software or create |br|
                        backups."];
        D [label = "Upload ?", shape="diamond",
           description="If you want to upload your modifications to your |br|
                        personal repository, you shoud use the :code:`git push` |br|
                        command. Otherwise, you can continue to add |br|
                        commits."];
        E [label = "Finished ?", shape="diamond",
           description="If your work on the branch is done, you should |br|
                        submit your modifications to the official repository. |br|
                        Otherwise, you can continue to add commits."];
        F [label = "Submit", shape="roundedbox",
           description="See `Submit your modifications`_ section. In order |br|
                        to integrate your modifications to the official |br|
                        repository, you must submit your modifications |br|
                        that will be integrated by **StatisKit** mainteners."];
        
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

.. note::

    In the following we assume that you forked the official repository in your personal account and cloned it according to previous recommendations (see :doc:`fork`).

.. MngIt

.. |NAME| replace:: StatisKit

.. |BRIEF| replace:: meta-repository providing general documentation and tools for the **StatisKit** Organization

.. |VERSION| replace:: v0.1.0

.. |AUTHORSFILE| replace:: AUTHORS.rst

.. _AUTHORSFILE : AUTHORS.rst

.. |LICENSENAME| replace:: CeCILL-C

.. |LICENSEFILE| replace:: LICENSE.rst

.. _LICENSEFILE : LICENSE.rst

.. MngIt
