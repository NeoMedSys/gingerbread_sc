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
