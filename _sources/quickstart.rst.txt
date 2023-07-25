Quickstart
==========

To get started with Gingerbread, researchers are required to follow these steps:

1. Clone the GitHub repository for the Gingerbread source files by executing the following command in the terminal (Note: Git needs to be installed):


```bash
git clone https://github.com/NeoMedSys/gingerbread_sc.git
```

1. Once the repository is cloned, researchers should make necessary alterations to the *central_processing.py* file, which contains the *prediction_step,* *preprocessing,* and *postprocessing* functions.

.. important::
    In the *central_processing.py* file, researchers must fill in the required code specific to their model to ensure proper functionality.

Add all other code needed in a structured way, use config files and other project structures as baseline of your implementation. Tests will be ran to ensure that the code is working properly with *NeoGate* before uploading.

2. After completing the necessary changes to the *central_processing.py* file use NeoGate to confirm that the code is working properly.

```bash
neogate test -p /gingerbread
```
.. important::
    The folder needs to be named *gingerbread*, this means basically removing *_sc* from the folder name.

If the code is working properly, researchers should see the following output:

```bash
Test passed!
```
3. The model will the be built appropriately and uploaded to the NeoMedSys Dockerhub repository. To do this, researchers should execute the following command in the terminal:

.. important::
    You need to have docker installed on your machine for this process to work.

4. Researchers should then create a new GitHub repository for their model and push the code to the new repository.

