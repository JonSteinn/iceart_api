******
iceart
******

|Build badge| |Test badge| |Codecov badge|

.. |Build badge| image:: https://github.com/jonsteinn/iceart_api/workflows/build/badge.svg
   :target: https://github.com/JonSteinn/iceart_api/actions?query=workflow%3Abuild

.. |Test badge| image:: https://github.com/jonsteinn/iceart_api/workflows/tests/badge.svg
   :target: https://github.com/JonSteinn/iceart_api/actions?query=workflow%3Atests

.. |Codecov badge| image:: https://codecov.io/gh/jonsteinn/iceart_api/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/jonsteinn/iceart_api

Dev setup
#########
To get started, run

.. code-block:: bash

    ./script/dev_setup.bat # win
    ./script/dev_setup.sh  # unix

You can do so using a venv if you so choose.

To start the app, run:

.. code-block:: bash

    python -m iceart.main  # win
    python3 -m iceart.main # unix

Other things to consider
************************
To use the database, you should create a `.env` file in the project root directory and set the following values.

.. code-block:: bash

    ICEART_DB_USER=__TODO__
    ICEART_DB_PW=__TODO__
    ICEART_DB_PATH=__TODO__
