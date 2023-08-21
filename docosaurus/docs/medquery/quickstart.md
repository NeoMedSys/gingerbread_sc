---
sidebar_position: 1
---

# Quickstart ✌

:::danger Not ready
This feature is in alpha and not ready for use.
:::

Gingerbread comes with medquery and the certificates to access the database already installed.

Here is an example code for downloading data.

```python title="python"
import data_download as dd

mqd = dd.MedqueryDataDownloader()
mqd.download_data(
                project_id="booby",
                get_affines=True,
                get_all=True,
                include_mask=False,
                batch_size=20
                )
```

This will download the data into ./data and add it to a hdf5 file. hdf5 files are storage files that simulates a harddrive. This makes it easier to store and lazy load during training. Check out the documentation here: https://docs.h5py.org/en/stable/

We have also included two functions to convert the hdf5 files to nifti. This is useful if you want to use the data in other software. The functions are hdf5_to_nifti_all and hdf5_to_nifti_single. The first one will convert all the data in the hdf5 file to nifti. The second one will convert a single image.

For more information check out the reference api in the documentation.
