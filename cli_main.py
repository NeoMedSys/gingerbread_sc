import torch
from typing import Dict, List, Optional, Tuple, Union, Any, cast, NoReturn
from torch import Tensor
import numpy as np
import argparse

import central_processing as cpr


def main() -> NoReturn:
    """
    Main function for the central processing unit.
    Configure the central processing unit with the command line arguments.
    Add the command line arguments to the central processing unit as you see fit.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--lr", type=float, default=4e-4)
    parser.add_argument("--config", type=str, default="config.yaml")
    args = parser.parse_args()

    cpr.CentralProcessing(args)


if __name__ == "__main__":
    main()