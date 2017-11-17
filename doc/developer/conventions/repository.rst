How to organize a repository
############################

In order to help mainteners, a certain directory structure must be conserved within all repositories.

+------------------------------------+----------------------------------------------------------------------------------------------------+
| Directory                          | Description                                                                                        |
+====================================+====================================================================================================+
| :code:`/`                          | Repository root directory                                                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/bin`                       | Essential files that need to be available for mainteners                                           |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/bin/conda`                 | **Conda** recipes for generating **Conda** binaries                                                |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/bin/docker`                | **Docker** contexts for generating **Docker** images containing generated **Conda** binaries       |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/doc`                       | Essential files that need to be available for documenters                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/share`                     | Essential files that need to be available for users                                                |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/share/git`                 | **Git** sub-modules that need to be available for users                                            |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/share/jupyter`             | **Jupyter** notebooks that need to be available for users                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/src`                       | Essential files that need to be available for developers (*s.s*)                                   |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/src/cpp`                   | *C++* source code                                                                                  |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/src/cpp/SConscript`        | **SCons** configuration file for the *C++* source code compilations and installations              |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/src/py`                    | *Python* source code                                                                               |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/src/py/wrapper`            | *Boost.Python* source code for interfacing the *C++* source code with *Python*                     |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/src/py/wrapper/SConscript` | **SCons** configuration file for the *Boost.Python* source code compilations and installations     |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/test`                      | Essential files that need to be available for testers                                              |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/travis.yml`                | **Travis CI** configuration file                                                                   |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/.travis.yml`               | A symbolic link to the **Travis CI** configuration file                                            |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/appveyor.yml`              | **Appveyor CI** configuration file                                                                 |
+------------------------------------+----------------------------------------------------------------------------------------------------+
| :code:`/SConstruct`                | **SCons** input file                                                                               |
+------------------------------------+----------------------------------------------------------------------------------------------------+
.. toctree::
    :maxdepth: 2

    c++_python
    python

.. warning::

    
These conventions concern recommended files and directories that should be present in a repository:

.. blockdiag::
    :align: center
    :desctable:
    
    blockdiag {

        A [label = "conda", shape="roundedbox",
           description=""];

        AA [label = "libXXX", shape="roundedbox",
           description=""];

        AB [label = "python-XXX", shape="roundedbox",
           description=""];

        B [label = "doc", shape="roundedbox",
           description=""];

        BA [label = "install", shape="roundedbox",
           description=""];

        BB [label = "examples", shape="roundedbox",
           description=""];

        BB [label = "faq", shape="roundedbox",
           description=""];

        C [label = "docker", shape="roundedbox",
          description=""];

        D [label = "docker", shape="roundedbox",
          description=""];

        DA [label = "docker", shape="roundedbox",
          description=""];

        DB [label = "docker", shape="roundedbox",
          description=""];


        A -> AA, AB;

        B -> BA, BB;

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

        D -> DA, DB;

        E -> F;

        G;

        H;

        I;

        J;

        K;

        L;

        M;

        N;

        O;

        P;

        doc -> install, examples, faq;
        docker;
        src -> cpp, py;
        test -> test_XXX.py;


        }

A
            conda -> ;

            conda -> bld.bat;
            conda -> build.sh;
            conda -> INSTALL.BAT;
            conda -> INSTALL.SH;
            conda -> UPLOAD.BAT;
            conda -> UPLOAD.SH;

        A;

            A -> AA;
            A -> AB;
            A -> AC;
            A -> AD;

        B;

            C -> CA;
            C -> CB;

        C;

        D;

        E;
    }






Ab
  /
   doc/
       conf.py
       Makefile
       make.bat
       requirements.txt
       index.rst
   src/
   AUTHORS.rst
   LICENSE.rst
   README.rst
