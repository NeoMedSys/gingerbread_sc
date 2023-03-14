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

    def __init__(self, args: argparse.Namespace) -> NoReturn:
        """Constructor for the central processing unit."""
        super().__init__()
        self.args = args
        # self.save_hyperparams()

    def postprocess(
        self, data: Dict[str, np.ndarray], stage: str, extras: Dict[str, Any] = {}
    ) -> Tensor:
        """Postprocess the data after training/val/test/predict

        Parameters
        ----------
        data : dict
            the data to be postprocessed
        stage : str
            the stage of the postprocessing, e.g. "train", "val", "test", "predict"
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
        Tensor
            the postprocessed data
        """
        resolution = extras.get("resolution", None)
        self.logga.info(f"Postprocessing data for stage {stage}")
        try:
            # Fill here
            pass
        except Exception as e:
            self.logga.error(f"Postprocessing failed for stage {stage} with error {e}")
        return data

    def preprocess(
        self, data: Dict[str, Tensor], stage: str, extras: Dict[str, Any] = {}
    ) -> dict:
        """Preprocess the data before training/val/test/predict

        Parameters
        ----------
        data : dict
            the data to be preprocessed
        stage : str
            the stage of the preprocessing, e.g. "train", "val", "test", "predict"
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
        dict
            the preprocessed data
        """
        resolution = extras.get("resolution", None)

        self.logga.info(f"Preprocessing data for stage {stage}")
        try:
            if not all(stage in cfg.STAGES for s in cfg.STAGES):
                self.logga.warning(f"stage must be one of {cfg.STAGES}, got {stage}")
                raise ValueError(f"stage must be one of {cfg.STAGES}, got {stage}")

            if stage == "predict":
                data = AddChanneld(keys=self.key_input)(data)
                data = ScaleIntensityd(keys=self.key_input, channel_wise=True)(data)
                data = ToTensord(keys=self.key_input, dtype=torch.float32)(data)

            else:
                # data =LoadImaged(keys=[self.key_input, self.key_label])
                data = AddChanneld(keys=[self.key_input, self.key_label])(data)
                data = ScaleIntensityd(keys=self.key_input, channel_wise=True)(data)
                data = ToTensord(
                    keys=[self.key_input, self.key_label], dtype=torch.float32
                )(data)
            return data
        except Exception as e:
            self.logga.error(f"Postprocessing failed for stage {stage} with error {e}")

    def predict_step(self, batch: Tensor) -> Dict[str, np.ndarray]:
        """
        Predict step function.

        Parameters
        ------------
        batch: Tensor
            Batch.
        batch_idx: int
            Batch index.
        dataloader_idx: int
            Dataloader index.

        Returns
        ------------
        y_pred: np.ndarray
            Predictions.
        """
        try:
            self.eval()
            with torch.no_grad():
                y_pred = self.infer(batch[self.key_input], self.model)
            return {"y_pred": y_pred}
        except Exception as e:
            self.logga.error(f"Could not predict: {e}")
