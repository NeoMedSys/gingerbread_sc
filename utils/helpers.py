# external
from typing import Callable
from functools import wraps
from time import time
from loguru import logger


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
        logger.info("Runtime for {}: {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper
