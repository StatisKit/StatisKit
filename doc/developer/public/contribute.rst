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

        E -> B [label = "No"];
            
            D -> E;
            D -> A [label = "Yes"];
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
