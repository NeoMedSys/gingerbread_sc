import os
from typing import Tuple, Dict
from pydantic import BaseModel as PydanticBaseModel
import torch

# data stages
STAGES = ["train", "val", "test", "predict"]
INPUT_KEY_LABEL = "y"
INPUT_KEY_IMAGE = "x"

ROOT: os.PathLike = os.getcwd()

REQUIRED_SHAPE = 3

# EXTRAS
DATA_SAVE_DIR = "./data"

#github repo metadata
PROJECTMETADATAURL = "https://raw.githubusercontent.com/NeoMedSys/gingerbread_sc/main/pyproject.toml"


class BaseModel(PydanticBaseModel):
    class Config:
        arbitrary_types_allowed = True


class ModelInput(BaseModel):
    model: torch.nn.Module