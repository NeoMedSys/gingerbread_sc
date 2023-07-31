import torch
from typing import Dict, Any
import numpy as np
from beartype.typing import Dict, Optional, Any, NoReturn
from neolibrary.monitoring.logger import NeoLogger

from utils.helpers import timer
from config import config
from neotemplate.base_central_processing import CPNeoTemplate


logger = NeoLogger(__name__).get_logger()

class CentralProcessing(CPNeoTemplate):
    """
    Central processing unit for preprocessing, postprocessing, predicting and training.


    Parameters
    ------------
    args: argparse.Namespace
        The arguments for the central processing unit.


    Warning
    ------------
    Remember to include methods for preprocessing, postprocessing, predict_step or you will get an error.

    """

    def __init__(self) -> NoReturn:
        """Constructor for the central processing unit."""
        super().__init__()
        logger.info('Initializing central processing unit')
        self.test_data = np.random.randn(
            32, 32, 32
        )  # Please make sure this data mimics your own data

    @timer
    def preprocess(
        self, data: np.ndarray, extras: Optional[Dict[str, Any]] = {}
    ) -> np.ndarray:
        """Preprocess the data before training/val/test/predict.

        Parameters
        ----------
        data : np.ndarray
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

        try:
            logger.info(f'Preprocessing data with shape {data.shape}')

            # --------------------- #
            # TODO: Your preprocessing code here
            # --------------------- #

            logger.success('=> Preprocessing completed successfully')
            return data
        except (NameError, ValueError, TypeError, AttributeError, RuntimeError) as e:
            msg = f'I failed preprocessing the image with error: {e}'
            logger.exception(msg)
        except Exception as e:
            msg = f'I failed preprocessing the image. Unexpected exception: type={type(e)}, e:{e}'
            logger.exception(msg)

    @timer
    def predict_step(self, data: np.ndarray, model: config.ModelInput) -> np.ndarray:
        """
        Predict step function.

        Parameters
        ------------
        data: np.ndarray
            data input

        Returns
        ------------
        np.ndarray
            Predictions.
        """
        try:
            self.eval()
            with torch.no_grad():
                logger.info(f'Predicting data with shape {data.shape}')
                data = model(data)
                # --------------------- #
                # TODO: Your prediction code here
                # --------------------- #

                logger.success('=> Prediction completed successfully')
                return data
        except (
            NameError,
            ValueError,
            TypeError,
            AttributeError,
            RuntimeError,
        ) as e:
            msg = f'I failed predicting the image with error: {e}'
            logger.exception(msg)
        except Exception as e:
            msg = f'I failed predicting the image. Unexpected exception: type={type(e)}, e:{e}'
            logger.exception(msg)

    @timer
    def postprocess(
        self, data: np.ndarray, extras: Optional[Dict[str, Any]] = {}
    ) -> np.ndarray:
        """Postprocess the data after training/val/test/predict

        Parameters
        ----------
        data : np.ndarray
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
            logger.info(f'Postprocessing data with shape {data.shape}')

            # --------------------- #
            # TODO: Your postprocessing code here
            # --------------------- #

            logger.success('=> Postprocessing completed successfully')
            return data
        except (
            NameError,
            ValueError,
            TypeError,
            AttributeError,
            RuntimeError,
        ) as e:
            msg = f'I failed postprocessing with error {e}'
            logger.exception(msg)
        except Exception as e:
            msg = f'I failed postprocessing the image. Unexpected exception: type={type(e)}, e:{e}'
            logger.exception(msg)
