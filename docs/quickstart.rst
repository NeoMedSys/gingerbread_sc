Quickstart
==========

1. Make sure you are logged in with a dockerhub account that can access our private dockerhub repository.

    ``docker login -u gingerbread01``

.. important::
        
        You need a password to login, please contact us if you don't have one.

2. Pull the latest version of the docker image:

   ``docker pull gingerbread:latest``

3. Run the docker image, use enable all gpus and mount the current directory to your project directory:

   ``docker run -it --gpus all gingerbread:latest /bin/bash``

.. hint::
    
        You can use VSCode to connect to the docker container and edit the code in the container.

        If you do not use VSCode or have access to the docker through VSCode, you can use argument ``-v <path to your project>:/project`` to mount your project directory to the docker container. You can now move ``/gingerbread/*`` to ``/project`` and edit the code in your project directory. 

        .. important::
            
            If you use this method, you put this folder back to ``/gingerbread`` before you commit your image. In production we will use the docker image without your project directory mounted.

            When you move a folder with poetry environment you will need to run ``poetry update`` in your new folder to update the poetry environment.

4. The docker image contains a poetry environment, you can activate it with:

   To run code use: ``poetry run python main.py``, this will run the code in the poetry environment. To install new packages, use ``poetry add <package>`` and to remove packages use ``poetry remove <package>``. Read more on poetry here: https://python-poetry.org/docs/basic-usage/.


.. hint::
        
        If you want to use pytorch-lightning, you will need to add it with ``poetry add pytorch-lightning``. If you want to use CLI version of pytorch-lightning, use ``poetry add pytorch-lightning[extra]``.
        You can find the lightning template in /lightning with the corresponding data loader templates.
   

