import os
from typing import Tuple, Dict
from central_processing import CentralProcessing

# data stages
STAGES = ["train", "val", "test", "predict"]
INPUT_KEY_LABEL = "y"
INPUT_KEY_IMAGE = "x"

ROOT: os.PathLike = os.getcwd()

# Batch extraction
BATCH_SIZE = 4
SPOTTY_BATCH_PATH = "spotty_batch.py"
BATCH_SIZE = int(os.environ.get("BATCH_SIZE", 4))
# BATCH_QUERY_LIMIT = int(os.environ.get("BATCH_QUERY_LIMIT", 4))

# ---------------------------------------------------------
WEIGHTS_DIR = os.path.join(ROOT, "model_weights")
WEIGHTS_PATH = os.path.join(WEIGHTS_DIR, "epoch=4950-dice_mean=78.49.pth")

MODELS = {
    "DynUnet": CentralProcessing,
}

# ---------------------------------------------------------
SQL_FILE_PATH_MODELS_WEIGHTS = os.path.join(ROOT, "sql/extract_model_weights.sql")
SQL_FILE_PATH_BATCH = os.path.join(ROOT, "sql/extract_series_uid.sql")
SQL_FILE_PATH_REALTIME = os.path.join(ROOT, "sql/extract_realtime.sql")

REST_PORT = 5378
ALL = ["*"]
API_BASE_URL = "http://localhost"
ORIGINS = [
    "".join(API_BASE_URL),
    "".join((API_BASE_URL, ":", str(REST_PORT))),
    "".join((API_BASE_URL, ":", str(REST_PORT), "/spotty-rest-api")),
    "".join((API_BASE_URL, ":", str(REST_PORT), "/check-connection")),
    "".join((API_BASE_URL, ":", str(REST_PORT), "/cache-invalidate")),
]

TOKEN: str = os.environ.get("REST_TOKEN")

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
# MRSAL
MRSAL_HOST = "localhost"
MRSAL_EXCHANGE = "exchangeRT"
MRSAL_EXCHANGE_TYPE = "topic"
MRSAL_CREDENTIALS: Tuple[str, str] = (
    os.environ.get("RABBITMQ_DEFAULT_USER"),
    os.environ.get("RABBITMQ_DEFAULT_PASS"),
)
MRSAL_BINDING_KEY = "exchangeRT.spotty"
MRSAL_QUEUE = "spottyQueue"
REQUEUE = False
MRSAL_PORT = 5672
VIRTUAL_HOST = "myMrsalHost"

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

# ---------------------------------------------------------
# Beaker cache
CACHE_TYPE = "file"
CACHE_EXPIRE_SEC = 86400  # 24 hours
CACHE_NAMESPACE = "cache_namespace"
CACHE_DATA_DIR = os.path.join(ROOT, "cache/data")
CACHE_LOCK_DIR = os.path.join(ROOT, "cache/lock")
# ---------------------------------------------------------

# ---------------------------------------------------------
# EXTRAS
DATA_SAVE_DIR = "./data"

#github repo metadata
PROJECTMETADATAURL = "https://raw.githubusercontent.com/NeoMedSys/gingerbread_sc/main/pyproject.toml"