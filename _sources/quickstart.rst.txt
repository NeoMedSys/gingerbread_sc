Quickstart
==========

1. Make sure you are logged in with a dockerhub account that can access our private dockerhub repository.

   ``docker login -u gingerbread01``

.. important::
        
        You need a password to login, please contact us if you don't have one.

2. Download the source code from github.

   ``git clone https://github.com/NeoMedSys/gingerbread_sc.git``

3. Make sure you are in the root directory of the project:

   ``cd gingerbread_sc``

4. Add the UID and GID to the docker container by sourcing the ``environment.env`` file with shell:

   ``. environment.env``

.. hint::
         
         If you are using powershell, use ``source environment.env`` instead.

5. Run docker compose to start the container:

   with cpu: ``docker compose up -d cpu``

   with gpu: ``docker compose up -d gpu``
   

6. Open a terminal in the container:

   ``docker exec -it ginger /bin/bash``

.. attention::
   The docker image contains a poetry environment, you can activate it with:

   To run code use: ``poetry run python main.py``, this will run the code in the poetry environment. To install new packages, use ``poetry add <package>`` and to remove packages use ``poetry remove <package>``. Read more on poetry here: https://python-poetry.org/docs/basic-usage/.

7. Install the poetry environment:

   ``poetry install``

.. hint::
        
        If you want to use pytorch-lightning, you will need to add it with ``poetry add pytorch-lightning``. If you want to use CLI version of pytorch-lightning, use ``poetry add pytorch-lightning[extra]``.
        You can find the lightning template in /lightning with the corresponding data loader templates.
   

You are now ready to start coding!

Here is a breakdown of the files in the project:

``central_processing.py``: This is the model template, it uses the basic ``pytorch.nn`` module to define the model. You can work as you would normally do with ``pytorch``, the only difference is that you need to define the ``preprocessing``, ``postprocessing`` and ``predict_step``. We will be using these functions in production, so make sure they are defined correctly and do not change their method names.

``cli_main.py``: This a template for using cli arguments. You can costumize as you want and if you want to use it.

``data_download.py``: With this you can download data from medquery, check out the documentation here: :doc:`medquery`

``central_processing_handler.py``: This is the bridge between the researchers model and production. 

.. danger::
   Do not make any changes to ``central_processing_handler.py``.
