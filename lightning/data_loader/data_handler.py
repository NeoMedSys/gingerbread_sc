import numpy as np
from torch import Tensor
from dataclasses import dataclass
from typing import Dict, Union
import coloredlogs, verboselogs


@dataclass
class DataHandler:
    """
    Data handler for training, validation, and test datasets.
    This is where the data injection happens, edit as you see fit, but make sure to return a dictionary with the keys "x" and "y".
    
    Attributes
    ----------
    size: int
        The size of the image, e.g. 32x32
    length: int
        The length of the dataset
    data: np.ndarray
        The data to be injected
    medquery_pipe: None
        The medical query pipeline
    local_pipe: None
        The local pipeline
    
    Note
    ----
    You probably have to change this as you see fit, but make sure to return a dictionary with the keys "x" and "y".


    Methods:
    -------

    """
    size: int = 32
    length: int = 64*4
    data: np.ndarray = np.ones((length, 2, size, size))

    coloredlogs.install()
    logga = verboselogs.VerboseLogger(__name__)
    logga.info("Data handler initialized.")

    def __getitem__(self, index: int) -> Dict[str, Union[Tensor, np.ndarray]]:
        x, y = self.data[index]
        return {"x": x, "y": y}

    def __len__(self) -> int:
        return len(self.data)