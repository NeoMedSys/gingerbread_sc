import torch
from torch import Tensor
import torch.nn as nn
import coloredlogs, verboselogs
from typing import Dict, Optional, Any, NoReturn
import numpy as np
import yaml

from config import config as cfg

class CPNeoTemplate(nn.Module):
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
        self.key_input:str = cfg.INPUT_KEY_IMAGE
        self.key_label:str = cfg.INPUT_KEY_LABEL

        try:
            # check if preprocessing, postprocessing, predict_step is implemented
            if not hasattr(self, "preprocessing"):
                raise NotImplementedError("Please implement the preprocessing method.")
            if not hasattr(self, "postprocess"):
                raise NotImplementedError("Please implement the postprocessing method.")
            if not hasattr(self, "predict_step"):
                raise NotImplementedError("Please implement the predict_step method.")
            if not hasattr(self, self.key_input):
                raise NotImplementedError("Please implement the key_input attribute.")
            if not hasattr(self, self.key_label):
                raise NotImplementedError("Please implement the key_label attribute.")
            
        except NotImplementedError as e:
            self.logga.error(e)
        
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
        torch.save({"state_dict": self.state_dict(),
                    "hyperparameters": self.args},
                    checkpoint_path)



