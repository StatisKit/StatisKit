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
           description="See :ref:`contribute-branch` section. In order |br|
                        to enable code review from mainteners, the |br|
                        development must be short (i.e. one branch for one |br|
                        task such as new feature, bug fix...)."];
        B [label = "Work", shape="roundedbox",
           description="See :ref:`contribute-work` section. In order |br|
                        to benefit from tools developped by mainteners and |br|
                        ensure code quality, the development must respect |br|
                        some guidelines."];
        C [label = "Commit", shape="roundedbox",
           description="See :ref:`contribute-commit` section. Commits |br|
                        are snapshots of the repository. There are useful |br|
                        in particular for versionning software or create |br|
                        backups."];
        D [label = "Upload ?", shape="diamond",
           description="See :ref:`contribute-upload` section. In order |br|
                        save your modifications into your personal repository, |br|
                        you should upload them. Otherwise, you can continue |br|
                        to add commits."];
        E [label = "Submit ?", shape="diamond",
           description="See :ref:`contribute-submit` section. In order |br|
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
            D -> B [label = "Yes"];
        }
    }

.. |br| raw:: html

   <br />

.. note::

    In the following we assume that you forked the official repository in your personal account and cloned it according to previous recommendations (see :doc:`fork`).

.. toctree::
    :hidden:
    
    branch/index
    work/index
    commit/index
    upload/index
    submit/index
