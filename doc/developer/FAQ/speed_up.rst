.. _section-developer-FAQ-speed-up:

How to speed up build time ?
############################

For projects using **SCons** or developers using build systems in IDEs (see the :ref:`section-developer-FAQ-IDE` section), it is possible to speed up the build time by parallelizing most of *C++* compilations.
This is usually done using the :code:`-j<CPU_COUNT>` flag with **SCons**:
For example

.. code-block:: console

   scons -j6

will use, when possible, :math:`6` concurrent compilations.

.. warning::

    It is not recommended to set :code:`<CPU_COUNT>` to a value superior to your number of processors.
    From a console, you can see yout number of processors by typing the following command line in a *Python* interpreter:

    .. code-block:: python

       import multiprocessing
       multiprocessing.cpu_count()

To avoid using the :code:`-j<CPU_COUNT>` flag each time, you can type the following command line in your console:

.. code-block:: console

    cpu_count

This will automatically set the number of concurrent compilations to your number of processors minus one.
You can manually specify the number of concurrent compilations using the :code:`--number <CPU_COUNT>` flag.
