======================
Gingerbread
======================

.. image:: https://img.shields.io/badge/Python-3.9-blue
    :target: https://www.python.org/downloads/release/python-390
.. image:: https://img.shields.io/badge/PyTorch-1.13.1-blue
    :target: https://pytorch.org/
.. image:: https://img.shields.io/badge/Poetry-1.3.2-blue
    :target: https://python-poetry.org/
.. image:: https://img.shields.io/badge/Monai-1.1.0-blue
    :target: https://monai.io/

.. important::

    This sample documentation was generated on today, and is rebuilt weekly.

Introduction
=============

Hi, I'm Gingerbread, I am a template for researchers to to interact better with NeoMedSys.
I will try guide you through the process of creating a new project, and how to use the template.

.. note::

    This template is based on docker, and uses poetry to manage the python dependencies.

The template consists of three parts. 

The ``first`` part is the source files, these make up the code template for the researcher to use and works in tandem with the production pipeline. This makes it easier for the production team to work with the researchers and vice versa. 

This means that it's easier for the researchers to keep themselves updated on the standardization of the code.

The ``second`` part is the documentation, this is a guide for the researchers to follow to make sure that they are using the template correctly. By using this type of documentation for all projects makes it easier to reproduce the results, for new employees to get into the workflow and for everyone to understand what is going on.

The ``third`` part is the docker image, or the ``operating system`` if you will. This is the environment that the researchers will be working in. This makes it easier for the researchers work to fit more easily into the production pipeline.


Extra information
----

You just read a *note* block. You can use these to highlight information that is interesting. The documentation has all kinds of different block types, and you can use them to highlight different degrees of importance.

With Gingerbread, you use a docker container to containerize your project. This means that you can run your project on any machine, without having to worry about installing dependencies. You can also use the same container to run your project on a server, or on a cluster. This is very handy when setting up arbitrary models and experiments into a pipeline.

The template allows you to use pytorch or pytorch-lightning, the template is not complex, we added a class that inherits from a template which throws errors if certain functions are not implemented which are critical for the pipeline. 

So, if you feel ready, let's get started!
Head over to the :doc:`quickstart` page to get started.


Documentation
=============

.. toctree::
    :maxdepth: 1
    :caption: Documentation
    :titlesonly:

    quickstart
    medquery
    modules

.. toctree::
    :caption: NeoMedSys
    :titlesonly:
    
    https://neomedsys.io/ <https://neomedsys.io/>

.. -----

.. [1]_
.. .. [1] If you hit an error while building documentation with a new theme,
..     it is likely due to some theme-specific configuration in the ``conf.py``
..     file of that documentation. These are usually ``html_sidebars``,
..     ``html_theme_path`` or ``html_theme_config``. Unsetting those will likely
..     allow the build to proceed.
