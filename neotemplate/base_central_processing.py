import torch
import torch.nn as nn
from neolibrary.monitoring.logger import NeoLogger
from beartype.typing import Dict, Optional, Any, NoReturn
import numpy as np
import yaml
import toml
import requests
import sys

from config import config as cfg


logger = NeoLogger(__name__)


class CPNeoTemplate(nn.Module):
    """Central processing unit for the NeoTemplate."""

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
        logger.info('CentralProcessing initialized')
        self.check_version()

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
        with open('hyperparameters.yaml', 'w') as f:
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
        logger.info(f'Loading checkpoint from {checkpoint_path}')
        checkpoint = torch.load(checkpoint_path)
        self.load_state_dict(checkpoint['state_dict'])
        self.args = checkpoint['hyperparameters']

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
        logger.info(f'Saving checkpoint to {checkpoint_path}')
        torch.save(
            {
                'state_dict': self.state_dict(),
                'hyperparameters': self.args
            },
            checkpoint_path,
        )

    def postprocess(self, data: np.ndarray, extras: Optional[Dict[str, Any]] = {}) -> np.ndarray:
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
        np.ndarray
            the postprocessed data
        """
        try:
            raise NotImplementedError
        except Exception as e:
            logger.error(f'Postprocessing failed with error {e}')

    def preprocess(self, data: np.ndarray, extras: Optional[Dict[str, Any]] = {}) -> np.ndarray:
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
        np.ndarray
            the preprocessed data
        """
        extras.get('resolution', None)

        try:
            raise NotImplementedError
        except Exception:
            logger.error('preproccessing failed')

    def predict_step(self, data: np.ndarray) -> np.ndarray:
        """
        Predict step function.

        Parameters
        ------------
        data: np.ndarray
            Batch.

        Returns
        ------------
        np.ndarray
            Predictions.
        """

        try:
            raise NotImplementedError
        except Exception:
            logger.error('predict_step failed')

    def check_version(self):
        try:
            # Fetch the contents of the .toml file
            response = requests.get(cfg.PROJECTMETADATAURL, timeout=5)

            # Parse the contents of the .toml file
            toml_data = toml.loads(response.text)

            # Retrieve the version number from the parsed data
            version = toml_data['tool']['poetry']['version']

            # Compare the version number to the latest version on the public repository
            latest_version = toml.load('./pyproject.toml')['tool']['poetry']['version']
            if version != latest_version:
                logger.warning(
                    f'New version of Gingerbread source code is available: {version}, current version: {latest_version}, check updated documentation at https://neomedsys.github.io/gingerbread_sc/whatsnew.html'
                )

        except requests.exceptions.HTTPError as e:
            logger.error(f'Error in version check: {e}')
