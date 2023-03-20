import torch
from typing import Dict, List, Optional, Tuple, Union, Any, cast, NoReturn
from torch import Tensor
import numpy as np
import argparse
from monai.transforms import (
    AddChanneld,
    ScaleIntensityd,
    ToTensord,
)

import config.config as cfg
from neotemplate.base_central_processing import CPNeoTemplate


class CentralProcessing(CPNeoTemplate):
    """
    Central processing unit for preprocessing, postprocessing, predicting and training.


    Attributes
    ------------
    logga: verboselogs.VerboseLogger
        The logger for the central processing unit.


    Parameters
    ------------
    args: argparse.Namespace
        The arguments for the central processing unit.


    Warning
    ------------
    Remember to include methods for preprocessing, postprocessing, predict_step or you will get an error.

    """

    def __init__(self, args: argparse.Namespace = None) -> None:
        """Constructor for the central processing unit."""
        super().__init__()
        self.args = args
        # self.save_hyperparams() # this is for saving hyperparams

        ########################################################3
        # Tests
        mock_data = {
            "x": np.random.rand(10, 10, 10)
        }  # Please make sure this data mimics your own data
        self.test_structure(data=mock_data)

    def preprocess(
        self, data: Dict[str, np.ndarray], extras: Dict[str, Any] = {}
    ) -> Dict[str, np.ndarray]:
        """Preprocess the data before training/val/test/predict

        Parameters
        ----------
        data : dict
            the data to be preprocessed
        extras: dict
            additional arguments for preprocessing such as resolution information etc.
            If provided, explain in depth in the docstring of the input and the input type.
            Example of extras:
                resolution [list]: resolution of the image, e.g. {"resolution": [1.0, 1.0, 1.0]}

        Important
        -------
        Extras dictionary is something the researchers need to define. There has to be a proper explanation of what the extras dictionary is and what it contains, as shown in the example above.

        Returns
        -------
        Dict[str, np.ndarray]
            the preprocessed data
        """
        resolution = extras.get("resolution", None)

        try:
            self.logga.success(f"=> Preprocessing completed successfully")
            return data
        except TypeError as e:
            self.logga.error(f"Preprocessing failed, error {e}")

    def predict_step(self, data: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Predict step function.

        Parameters
        ------------
        data: Dict[str, np.ndarray]
            data input

        Returns
        ------------
        Dict[str, np.ndarray]
            Predictions.
        """
        try:
            self.eval()
            with torch.no_grad():
                self.logga.success(f"=> Prediction completed successfully")
                return data
        except TypeError as e:
            self.logga.error(f"Prediction failed: {e}")

    def postprocess(
        self, data: Dict[str, np.ndarray], extras: Dict[str, Any] = {}
    ) -> Dict[str, np.ndarray]:
        """Postprocess the data after training/val/test/predict

        Parameters
        ----------
        data : dict
            the data to be postprocessed
        extras: dict
            additional arguments for preprocessing such as resolution information etc.
            If provided, explain in depth in the docstring of the input and the input type.
            Example of extras:
                resolution [list]: resolution of the image, e.g. {"resolution": [1.0, 1.0, 1.0]}

        Important
        -------
        Extras dictionary is something the researchers need to define. There has to be a proper explanation of what the extras dictionary is and what it contains, as shown in the example above.

        Returns
        -------
        Dict[str, np.ndarray]
            the postprocessed data
        """
        resolution = extras.get("resolution", None)
        try:
            self.logga.success(f"=> Postprocessing completed successfully")
            return data
        except TypeError as e:
            self.logga.error(f"Postprocessing failed with error {e}")
