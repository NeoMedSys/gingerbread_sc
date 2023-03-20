General Information
===================

On this page you will find general information about the project.


How to go about?
--------------

So you've opened the container and are ready to begin working on your project.

The only difference here is that the :ref:`central processing` needs to be filled out according to your model's main pipeline, ``preprocessing``, ``predict step``, and ``postprocessing``. In other words, you can create your own files and train your model as usual, but when you want to go into production, you must ensure that the :ref:`central processing` is correctly filled out according to your model's main pipeline. Fill in the :ref:`central processing` as you go or at the end. You can change it as you go through the experiments to ensure that it produces the desired results.


.. important:: 
        The docker-compose file will mount the local folder to the container's '/gingerbread' so you can work on your project as if it were a local folder.


We import :ref:`central processing` in production and run the three methods with datastreams from various sources. As a result, it is critical that you correctly fill out the :ref:`central processing` with the appropriate rights type for both input and output.



The philosophy
--------------

The project's guiding principle is to give researchers a straightforward framework that is simple to utilize.

This framework includes built-in MedQuery certifications, eliminating the need to manually add them for every project.

The framework also has the usual packages like poetry, CUDA etc. installed, so you can start working on your project right away.

The framework is also designed to be easily extensible, so you can add your own packages and certifications as you see fit, which in turn will modulerize into the production pipeline.

Another aspect of the framework is that it is easier to have a common understanding of how it all operates both for experiments and in production through regular documentation and code updates.

The idea is also for researchers to add issues in the Github repository if there is any changes they would like to see in the framework, so that the framework can be improved over time and if there are any bugs or limitations.

