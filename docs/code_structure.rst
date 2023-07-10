Code structure
==========

.. info::
    This documentation discusses the code structure and idea behind the code.


The idea
--------
We want a simple way to for the developers of the models to be able to add their model to the production code.
The full *app* is built from many different *modules* grabbed from the private NeoMedSys dockerhub repository. The modules consists of python files and folders that are added together with the modified (by the model creators) *gingerbread* source code to the main docker image.

The different modules will import the files coming in from the different modules. Because of this, it could give errors if the modules are not compatible with each other.
The reason why we modularized the different parts of the *app* is because it will make it easier to update the different parts of the *app* for all the different models without having to change the the system code in each model, which are usually the same for all models.


The code structure
------------------
The code structure is as follows in the final docker image:

    .
    ├── *systemfolders*
    ├── gingerbread
    │   ├── config
    │   ├── neotemplate
    │   ├── tests
    │   ├── utils
    │   ├── xmodules
    │   ├── README.md
    │   ├── central_processing.py
    │   ├── cli_main.py
    │   ├── data_download.py
    │   ├── poetry.lock
    │   ├── pyproject.toml
    ├── application (These are the service modules such as )
    │   ├── appfile.py (this name is based on the service)
    │   ├── config
    │   ├── utils
    ├── central_processing_handler
    │   ├── central_processing_handler.py
    │   ├── config
    │   ├── utils
    │   ├── sql
    ├── analytics
    │   ├── analytics_module.py