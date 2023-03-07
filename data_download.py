from pymedquery import pymq
import os
import shutil
import numpy as np
import coloredlogs, verboselogs
from tqdm import tqdm
import h5py
import nibabel as nib
from typing import NoReturn

import config.config as cfg


class MedqueryDataDownloader:
    """
    MedqueryDataDownloader class for connecting to MedQuery and downloading data.

    Attributes
    ----------
    mq : pymq.PyMedQuery
            pymedquery instance
    log : verboselogs.VerboseLogger
        logger instance


    """
    def __init__(self):

        self.mq = pymq.PyMedQuery()
        coloredlogs.install()
        self.log = verboselogs.VerboseLogger(__name__)
        self.log.info("MedqueryDataDownloader initialized.")

        
    def download_data(self, 
                    project_id: str,
                    get_affines: bool = False,
                    get_all: bool = True,
                    include_mask: bool = False,
                    batch_size: int = 20
                    ) -> NoReturn:
        """Download data from MedQuery and save it to disk.

        Note
        ----
        Instanciate the class and use this method to download data from MedQuery and save it to disk. For more information about data extraction from MedQuery, see {INSERT LINK HERE}.

        Parameters
        ----------
        project_id : str
            Project ID
        get_affines : bool, optional
            Get affines, by default False
        get_all : bool, optional
            Get all, by default True
        include_mask : bool, optional
            Include mask, by default False
        batch_size : int, optional
            Batch size, by default 20

        Returns
        -------
        None

        """
        try:
            large_data = self.mq.batch_extract(get_all=get_all,
                                               get_affines=get_affines,
                                               project_id=project_id, 
                                               batch_size=batch_size, 
                                               include_mask=include_mask
                                               )

            if not os.path.exists(cfg.DATA_SAVE_DIR):
                os.makedirs(cfg.DATA_SAVE_DIR)
            self.log.info(f"Downloading data from MedQuery for project {project_id}")
            with h5py.File(f'./data/{project_id}.hdf5', 'w') as f:
                for batch in tqdm(large_data, desc="Saving data to disk..."):
                    for key, value in batch.items():
                        f.create_dataset(key, data=value)
                    
        except Exception as e:
            self.log.error(f"Error while downloading data from MedQuery: {e}")
    
    def hdf5_to_nifti_all(self, hdf5_path: str, output_dir: str) -> NoReturn:
        """Convert hdf5 file to nifti file.

        Parameters
        ----------
        hdf5_path : str
            Path to hdf5 file
        output_dir : str
            Path to output directory

        Returns
        -------
        None

        Attention
        ---------
        This method assumed that the hdf5 file contains affine matrices and data. If this is not the case, the method will not work.
        """
        try:
            # make output directory if it does not exist
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            with h5py.File(hdf5_path, 'r') as hdf5:
                for series_uid, value_ in hdf5.items():
                    if "affine" in series_uid:
                        continue
                    affine_uid = series_uid.replace("series", "affine")
                    data = hdf5[series_uid]
                    affine = hdf5[affine_uid]
                    self.log.info(f"Converting {series_uid} file to nifti file...")
                    img = nib.Nifti1Image(data, affine)
                    nib.save(img, os.path.join(output_dir, f"{series_uid}.nii.gz"))
        except IndexError as e:
            self.log.error(f"Error with hdf5 indexing: {e}")
    
    def hdf5_to_nifti_single(self, hdf5_path: str, output_dir: str, series_uid: str) -> NoReturn:
        """Convert single series to nifti file.

        Parameters
        ----------
        hdf5_path : str
            Path to hdf5 file
        output_dir : str
            Path to output directory
        series_uid : str
            Series UID

        Returns
        -------
        None

        Attention
        ---------
        This method assumed that the hdf5 file contains affine matrices and data. If this is not the case, the method will not work.
        """
        try:
            with h5py.File(hdf5_path, 'r') as hdf5:
                data = hdf5[series_uid]
                affine_uid = series_uid.replace("series", "affine")
                affine = hdf5[affine_uid]
                self.log.info(f"Converting {series_uid} file to nifti file...")
                img = pymq.utils.convert2nii(img=data, affine=affine)
                nib.save(img, os.path.join(output_dir, f"{series_uid}.nii.gz"))
        except Exception as e:
            self.log.error(f"Error while converting hdf5 to nifti: {e}")
