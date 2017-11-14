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

        C;

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
