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

Hello, my name is Gingerbread, and I am a template enabling researchers to better engage with NeoMedSys. 
I'll do my best to walk you through the steps involved in creating a new project and utilizing the template. 

.. note::

    This template is based on docker, and uses poetry to manage the python dependencies.

The template consists of three parts. 

The ``initial`` element consists of the source files, which together with the production process form the researcher's code template. This makes it simpler for both the production team and the research team to collaborate.

The documentation is the ``second`` component; it serves as a manual for the researchers to use in order to ensure proper use of the template. It is simpler to duplicate the findings, for new hires to learn the workflow, and for everyone to comprehend what is happening when this sort of documentation is used for all projects.

The docker image, or ``operating system``, if you will, is the ``third`` component. The setting in which the researchers will operate is as described. The work of the researchers can more readily integrate into the production process as a result.

.. image:: https://user-images.githubusercontent.com/24882057/225026458-f80a82cc-f019-4b25-ac3e-7d465ebba073.png
    :align: center

Extra information
----

.. note::

    This is a block of notes

Just now, you read a *block of notes*. They can be used to draw attention to noteworthy information. You may utilize the various block types in the documentation to emphasize varying levels of relevance.

While using Gingerbread, you containerize your project using a docker container. As a result, you may execute your project without worrying about installing dependencies on any computer. The same container may be used to execute your project on a server or in a cluster as well. For putting up arbitrary models and experiments in a pipeline, this is quite useful.

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
    conduct_and_info
    modules

.. toctree::
    :caption: NeoMedSys
    :titlesonly:
    
    https://neomedsys.io/ <https://neomedsys.io/>
    https://github.com/NeoMedSys/gingerbread_sc <https://github.com/NeoMedSys/gingerbread_sc>

.. -----

.. [1]_
.. .. [1] If you hit an error while building documentation with a new theme,
..     it is likely due to some theme-specific configuration in the ``conf.py``
..     file of that documentation. These are usually ``html_sidebars``,
..     ``html_theme_path`` or ``html_theme_config``. Unsetting those will likely
..     allow the build to proceed.
