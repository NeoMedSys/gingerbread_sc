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
    logga : verboselogs.VerboseLogger
        Logger for the data handler.
    
    Note
    ----
    You probably have to change this as you see fit, but make sure to return a dictionary with the keys "x" and "y".

    """

    coloredlogs.install()
    logga = verboselogs.VerboseLogger(__name__)
    logga.info("Data handler initialized.")

    def __getitem__(self, index: int) -> Dict[str, Union[Tensor, np.ndarray]]:
        x, y = self.data[index]
        return {"x": x, "y": y}

    def __len__(self) -> int:
        return len(self.data)


    def add_data(self, data: Dict[str,Union[float,int]]) -> None:
        """
        Add data to the data handler.
        """

        assert type(data) == dict, "Data must be a dictionary."
        assert "x" in data.keys(), "Data must have a key 'x'."
        assert "y" in data.keys(), "Data must have a key 'y'."

        self.data = data