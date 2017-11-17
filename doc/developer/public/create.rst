Create a new repository
#######################

.. warning::
    
    Only owners of the **StatisKit** organization can create new repositories.
    
To create a new repository use the :code:`statiskit create` command.
This command launches the following workflow in order to create a new repository on the StatisKit organization.
To perform this, :code:`statiskit create` uses the **PyGithub** package to access `GitHub` interface in `Python`.
    
.. blockdiag::
    :align: center
    :desctable:
    
    blockdiag {

        A [label = "Initialize", shape="roundedbox",
           description="See :ref:`create_initialize` section. The repository |br|
                        initialization create an empty repository in the **StatisKit** |br|
                        organization."];
        B [label = "Complete", shape="roundedbox",
           description="See :ref:`create_complete` section. In order to complete |br|
                        the empty repository, you must respect some guidelines |br|
                        concering repository structures and mandatory files."];
        C [label = "Activate", shape="roundedbox",
           description="See :ref:`create_activate` section. In order to enable |br|
                        code review from mainteners, some web-services must be |br|
                        activated."];

.. Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ..
..                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
.. Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ..
..                                                                       ..
.. This file is part of the AutoWIG project. More information can be     ..
.. found at                                                              ..
..                                                                       ..
..     http://autowig.rtfd.io                                            ..
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

    }

.. |br| raw:: html

   <br />
   
.. toctree::
    :hidden:
    
    initialize/index
    complete/index
    activate/index
