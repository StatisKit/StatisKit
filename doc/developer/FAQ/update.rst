How to update the development environment ?
###########################################

I you need to update your development environment, type the following command line in your console

.. code-block:: console

   conda update --all --no-pin -c statiskit/label/develop -c statiskit -c defaults --override-channels

.. warning::

   In this case, the development environment must first be activated

In the worst case scenario, you can first uninstall your development environment and re-install it.
To do so, type the following command lines in your console

.. code-block:: console

  conda env remove -n statiskit -y
  conda clean --all -y
  conda create -n statiskit statiskit -c statiskit/label/develop -c statiskit -c defaults --override-channels


.. warning::

   In this case, the development environment must first be deactivated
