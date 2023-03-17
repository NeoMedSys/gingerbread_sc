General Information
===================

On this page you will find general information about the project.


How to go about?
--------------

So you have now opened up the container and you are ready to start working on your project. 

You can now work as if it was a new normal project, the only difference here is that the :ref:`central_processing` needs to be filled out according to your model's main pipeline, `Preprocessing`, `predict_step` and `postprocessing`. In other words, you can make your own files and train your model as you normally would, but you need to make sure that the :ref:`central_processing` is filled out correctly according to your model's main pipeline when you want to go into production. You can fill out the :ref:`central_processing` as you go along or at the end. You can change it along the experiments to see that it has the intended results.

.. important:: 
        The docker-compose file will mount the local folder to `/gingerbread` in the container, so you can work on your project as if it was a local folder.


In production we import :ref:`central_processing` and run the three methods with datastreams coming from different source. Therefore, it is important that you fill out the :ref:`central_processing` correctly with the rights type for both input and output.



The philosophy
--------------

The project's guiding principle is to give researchers a straightforward framework that is simple to utilize.

This framework includes built-in MedQuery certifications, eliminating the need to manually add them for every project.

The framework also has the usual packages like poetry, CUDA etc. installed, so you can start working on your project right away.

The framework is also designed to be easily extensible, so you can add your own packages and certifications as you see fit, which in turn will modulerize into the production pipeline.

Another aspect of the framework is that it is easier to have a common understanding of how it all operates both for experiments and in production through regular documentation and code updates.

The idea is also for researchers to add issues in the Github repository if there is any changes they would like to see in the framework, so that the framework can be improved over time and if there are any bugs or limitations.

