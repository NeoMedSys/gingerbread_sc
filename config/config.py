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

# ---------------------------------------------------------
# pymedquery credentials
MQUSER = os.environ.get("MQUSER")
MQPWD = os.environ.get("MQPWD")
DATABASE = os.environ.get("DATABASE")
PGSSLKEY = os.environ.get("PGSSLKEY")
PGSSLCERT = os.environ.get("PGSSLCERT")
PGSSLROOTCERT = os.environ.get("PGSSLROOTCERT")
MQHOST = os.environ.get("MQHOST")
MQPORT = os.environ.get("MQPORT")

# ---------------------------------------------------------
ENVPATH: os.PathLike = os.environ.get("PATH")
CRON_ENV: Dict[str, str] = {
    "PATH": ENVPATH,
    "PYTHONPATH": ROOT,
    "MQUSER": MQUSER,
    "MQPWD": MQPWD,
    "DATABASE": DATABASE,
    "PGSSLKEY": PGSSLKEY,
    "PGSSLROOTCERT": PGSSLROOTCERT,
    "PGSSLCERT": PGSSLCERT,
}

# EXTRAS
DATA_SAVE_DIR = "./data"

#github repo metadata
PROJECTMETADATAURL = "https://raw.githubusercontent.com/NeoMedSys/gingerbread_sc/main/pyproject.toml"


class BaseModel(PydanticBaseModel):

    class Config:
        arbitrary_types_allowed = True


class ModelInput(BaseModel):
    model: torch.nn.Module