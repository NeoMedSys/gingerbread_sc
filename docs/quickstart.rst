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

5. Run docker compose to start the container:

   with cpu: ``docker compose up -d cpu``

   with gpu: ``docker compose up -d gpu``
   

6. Open a terminal in the container:

   ``docker exec -it ginger /bin/bash``

.. attention::
        
        Unix systems use a very well defined user system with different permission levels. You might end up with some permission problems if you make new files inside the container and try to access them from your host machine. To avoid this, make sure you always create new files from the host machine and not from inside the container. If the docker container creates the files then you will need to change the permissions of the files to be able to access them from the host machine. To do this, run the following command from the host machine:

        Get your user id: ``id -u`` on host machine and ``id -g`` on host machine

        Change the permissions of the files: ``sudo chown -R <user_id>:<group_id> <file_name>``

        for folders: ``sudo chown -R <user_id>:<group_id> <folder_name>``

        We are working on a solution to make this process easier.

7. Add medquery environment:

   ``source /certs/.env``


8. Install the poetry environment:

   ``poetry install``

.. hint::
        
        If you want to use pytorch-lightning, you will need to add it with ``poetry add pytorch-lightning``. If you want to use CLI version of pytorch-lightning, use ``poetry add pytorch-lightning[extra]``.
        You can find the lightning template in /lightning with the corresponding data loader templates.
   

.. attention::
   The docker image contains a poetry environment, you can activate it with:

   To run code use: ``poetry run python main.py``, this will run the code in the poetry environment. To install new packages, use ``poetry add <package>`` and to remove packages use ``poetry remove <package>``. Read more on poetry here: https://python-poetry.org/docs/basic-usage/.


You are now ready to start coding!

Here is a breakdown of the files in the project:

``central_processing.py``: This is the model template, it uses the basic ``pytorch.nn`` module to define the model. You can work as you would normally do with ``pytorch``, the only difference is that you need to define the ``preprocessing``, ``postprocessing`` and ``predict_step``. We will be using these functions in production, so make sure they are defined correctly and do not change their method names.

``cli_main.py``: This a template for using cli arguments. You can costumize as you want and if you want to use it.

``data_download.py``: With this you can download data from medquery, check out the documentation here: :doc:`medquery`

``central_processing_handler.py``: This is the bridge between the researchers model and production. 

.. danger::
   Do not make any changes to ``central_processing_handler.py``.
