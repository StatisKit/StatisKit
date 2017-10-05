How to organize a repository
############################

In order to help mainteners, a certain structure must be conserved within all repositories.
This structure is depending on the programming languages used within a repository source code.

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