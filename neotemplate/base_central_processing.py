import torch
from torch import Tensor
import torch.nn as nn
import coloredlogs, verboselogs
from typing import Dict, Optional, Any, NoReturn
import numpy as np
import yaml
from abc import ABC, abstractmethod

from config import config as cfg


class CPNeoTemplate(nn.Module, ABC):
    """Central processing unit for the NeoTemplate.

    Attributes:
    ----------
    logga: verboselogs.VerboseLogger
        The logger for the central processing unit.

    Methods:
    -------

    """

    def __init__(self) -> NoReturn:
        """Constructor for the central processing unit

        Parameters:
        ----------
        None

        Returns:
        -------
        None

        """
        super().__init__()

        # logger [color]
        coloredlogs.install()
        self.logga = verboselogs.VerboseLogger(__name__)
        self.logga.info("CentralProcessing initialized")
        self.key_input: str = cfg.INPUT_KEY_IMAGE
        self.key_label: str = cfg.INPUT_KEY_LABEL

    def save_hyperparams(self) -> NoReturn:
        """Save hyperparameters to a file.

        Parameters:
        ----------
        None

        Returns:
        -------
        None
        """
        # save hyperparameters to a file
        with open("hyperparameters.yaml", "w") as f:
            yaml.dump(self.args, f)

    def load_from_checkpoint(self, checkpoint_path: str) -> NoReturn:
        """Load a checkpoint.

        Parameters:
        ----------
        checkpoint_path: str
            The path to the checkpoint.

        Returns:
        -------
        None
        """
        self.logga.info(f"Loading checkpoint from {checkpoint_path}")
        checkpoint = torch.load(checkpoint_path)
        self.load_state_dict(checkpoint["state_dict"])
        self.args = checkpoint["hyperparameters"]

    def save_checkpoint(self, checkpoint_path: str) -> NoReturn:
        """Save a checkpoint.

        Parameters:
        ----------
        checkpoint_path: str
            The path to the checkpoint.

        Returns:
        -------
        None
        """
        # save with the state_dict and the hyperparameters
        self.logga.info(f"Saving checkpoint to {checkpoint_path}")
        torch.save(
            {"state_dict": self.state_dict(), "hyperparameters": self.args},
            checkpoint_path,
        )

    @abstractmethod
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
        try:
            raise NotImplementedError
        except Exception as e:
            self.logga.error(f"Postprocessing failed with error {e}")

    @abstractmethod
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
            raise NotImplementedError
        except Exception as e:
            self.logga.error(f"Preprocessing failed with error {e}")

    @abstractmethod
    def predict_step(self, data: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Predict step function.

        Parameters
        ------------
        data: Dict[str, np.ndarray]
            Batch.

        Returns
        ------------
        Dict[str, np.ndarray]
            Predictions.
        """

        try:
            raise NotImplementedError
        except Exception as e:
            self.logga.error(f"Predict_step failed with error {e}")

    def test_structure(self, data: Dict[str, np.ndarray]) -> NoReturn:
        """Test the structure of the model.

        Parameters:
        ----------
        data: Dict[str, np.ndarray]
            The data to be tested.

        Returns:
        -------
        None
        """
        try:
            if isinstance(data, dict):
                for key, value in data.items():
                    if not isinstance(value, np.ndarray):
                        raise TypeError(
                            f"Data input is not a dictionary of numpy arrays. Key: {key} is of type {type(value)}"
                        )
            else:
                raise TypeError("Data input is not a dictionary")

            data = self.preprocess(data=data)
            if isinstance(data, dict):
                for key, value in data.items():
                    if not isinstance(value, np.ndarray):
                        raise TypeError(
                            f"Data input is not a dictionary of numpy arrays. Key: {key} is of type {type(value)}"
                        )
            else:
                raise TypeError("Data input from preprocess is not a dictionary")

            data = self.predict_step(data=data)
            if isinstance(data, dict):
                for key, value in data.items():
                    if not isinstance(value, np.ndarray):
                        raise TypeError(
                            f"Data input is not a dictionary of numpy arrays. Key: {key} is of type {type(value)}"
                        )
            else:
                raise TypeError("Data input is not a dictionary")
            data = self.postprocess(data=data)
            if isinstance(data, dict):
                for key, value in data.items():
                    if not isinstance(value, np.ndarray):
                        raise TypeError(
                            f"Data input is not a dictionary of numpy arrays. Key: {key} is of type {type(value)}"
                        )

        except Exception as e:
            self.logga.error(f"Test structure failed with error: {e}")
