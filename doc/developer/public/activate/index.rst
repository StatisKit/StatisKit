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

.. _create_activate:

Activate repository services
============================

If you look at the :code:`README.rst` file of the created repository, some web-services must be activated in order to obtain to respect **StatisKit** standards.
These services are:

* **Travis CI**.
  This `service <https://docs.travis-ci.com/>`_ is used to perform `continuous integration <https://en.wikipedia.org/wiki/Continuous_integration>`_ of repositories.
* **Coveralls**.
  This `service <https://coveralls.zendesk.com/hc/en-us>`_ is used to show which parts of your code aren't covered by repository `test suites <https://en.wikipedia.org/wiki/Test_suite>`_.
* **Landscape**.
  This `service <https://docs.landscape.io/index.html>`_ is used to perform `static analysis <https://en.wikipedia.org/wiki/Static_program_analysis>`_ of your code within repositories.
* **Read The Docs**.
  This `service <http://docs.readthedocs.io/en/latest/>`_ is used to ensure that documentation of your code is uploaded to repository documentation websites.
