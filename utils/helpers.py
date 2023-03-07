# external
import numpy as np
import blosc
import pickle as pkl
import base64
import gzip
import json
from uuid import uuid4
import datetime
from io import BytesIO
from collections import defaultdict
from typing import NoReturn, List, Union, IO, Dict, Callable, OrderedDict, Tuple
from pymedquery.pymq import PyMedQuery
from functools import wraps
from time import time
import coloredlogs, verboselogs
import torch
from copy import deepcopy

# internal
from config import config
from config.exceptions import (
    DatabaseUploadError,
    DatabasePrepareRecordError,
)

coloredlogs.install()
log = verboselogs.VerboseLogger(__name__)


def timer(orig_func: Callable):
    """This is custom timer decorator.
    Parameters
    ----------
    orig_func : object
        The `orig_func` is the python function which is decorated.
    Returns
    -------
    type
        elapsed runtime for the function.
    
    """

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = orig_func(*args, **kwargs)
        t2 = time() - t1
        print("Runtime for {}: {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper

def get_img_info(img: np.ndarray) -> Tuple[int, int, int]:
    """get_img_info is very simple helper that returns the dimension of image volume.

    Parameters
    ----------
    img : np.ndarray
        this is the image volume that you need to know the dimension for
    """
    try:
        height, width, depth = img.shape
    except ValueError:
        log.error("Image is not 3D")
        raise ValueError
    return height, width, depth


def decode_payload(payload: str, blosc_compression: bool = True) -> np.ndarray:
    """the function decodes a payload/response from the RadiomPipe API by first converting
    the hexstring to bytes and decompressing + decoding the buffer. The payload is then converted
    back to a dictionary from bytes.

    Parameters
    ----------
    payload : str
        the payload is the response from the RadiomPipe application
    Returns
    -------
    The dictionary contains two dataframes with radiomic features and diagnostic from the process as well
    as two dictionaries with masks from the segmentation and nested radiomics features.

    """
    if payload:
        if blosc_compression:
            # decode the buffer
            payload_b = bytes.fromhex(payload)
            payload_b = blosc.decompress(base64.b64decode(payload_b))
            return pkl.loads(payload_b)
        else:
            # slow but compresses better compared to blosc
            payload.seek(0)
            payload_b = gzip.decompress(payload.getvalue())
            array = np.frombuffer(payload_b)
            return np.reshape(array, payload.metadata)
    else:
        log.error("no payload received")
        raise ValueError

def decode_weights(encoded_weights: bytes) -> OrderedDict:
    """the function decodes a encoded weights loaded from MQ.
    
    Parameters
    ----------
    encoded_model : bytes
        encoded weights loaded from MQ.
    Returns
    -------
    weights : OrderedDict
        the weights of pre-trained model.
    """
    try:
        weights_bytes = blosc.decompress(base64.b64decode(encoded_weights))
        weights_dict = json.loads(weights_bytes)
        weights = {}

        """
        In order to take the "tensors" from the encoded objects, we need to apply:
        1. json.loads to get the list which represents the encoded tensor and its size
        2. base64.b64decode to convert str to bytes
        3. np.frombuffer to convert bytes to ndarray
        4. torch.from_numpy to convert from ndarray to tensor
        4. torch.reshape to reshape the tensor
        """
        for k, v in weights_dict.items():
            v_list = json.loads(v)
            tensor_size: torch.Size = v_list[0]
            arr_str: str = v_list[1]
            arr_bytes: bytes = base64.b64decode(arr_str)
            np_arr: np.ndarray = np.frombuffer(arr_bytes, dtype=np.float32)
            tensor = torch.reshape(torch.from_numpy(np_arr), tensor_size)
            weights[k] = tensor

        return weights
    except (NameError, ValueError, TypeError) as e:
        log.error("Error decoding weights: {}".format(e))
        raise e
    except Exception as e:
        log.error("Error decoding weights: {}".format(e))
        raise e



def check_version():
    log.info(f"PyTorch version: {torch.__version__}")




def welcome_logo():
    output = """
   ___ _                       _                        _ 
  / _ (_)_ __   __ _  ___ _ __| |__  _ __ ___  __ _  __| |
 / /_\/ | '_ \ / _` |/ _ \ '__| '_ \| '__/ _ \/ _` |/ _` |
/ /_\\| | | | | (_| |  __/ |  | |_) | | |  __/ (_| | (_| |
\____/|_|_| |_|\__, |\___|_|  |_.__/|_|  \___|\__,_|\__,_|
               |___/                                      
               """
    log.success(output)


if __name__ == "__main__":
    welcome_logo()