# global imports
import numpy as np
from typing import Dict, List, Tuple, Union, Any
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
import coloredlogs, verboselogs
import pymedquery as pymq
import torch
import torch.nn as nn

# local imports
import central_processing as cpr
import config.config as config  
from utils.helpers import (
                          timer,
                          decode_weights,
                          )



# Create the CacheManager instance to cache the model loaded from MQ
cache_opts = {
    "cache.type": config.CACHE_TYPE,
    "cache.data_dir": config.CACHE_DATA_DIR,
    "cache.lock_dir": config.CACHE_LOCK_DIR,
}
cache = CacheManager(**parse_cache_config_options(cache_opts))


class CentralProcessingHandler:
    """CentralProcessingHandler
    
    This class is the interface between the central processing and the rest of the code.
    It is responsible for loading the central processing model and for calling the
    appropriate functions.

    Attributes
    ------------
    cpr: central_processing.CentralProcessing
        The central processing model.
    device: torch.device
        The device to use for the central processing model.
    log: verboselogs.VerboseLogger
        The logger for the central processing handler.

    Parameters
    ------------
    None

    """
    def __init__(self):
        # logging
        coloredlogs.install()
        self.log = verboselogs.VerboseLogger(__name__)
        if torch.cuda.is_available():
            self.log.info("CUDA support enabled")
            self.log.info(f"I found {torch.cuda.device_count()} gpu devices available")
            gpu_id = torch.cuda.current_device()
            self.device = torch.device(f"cuda:{gpu_id}")
        else:
            self.log.info("No CUDA support found")
            self.device = torch.device("cpu")

    @cache.cache(config.CACHE_NAMESPACE, expire=config.CACHE_EXPIRE_SEC)
    def __get_model_from_mq(self):
        self.log.info(
            f"Getting the weights of pre-trained model from MQ: project_id = {config.PROJECT_ID} and model_version = {config.MODEL_VERSION}"
        )
        format_params = {
            "project_id": config.PROJECT_ID,
            "model_version": config.MODEL_VERSION,
        }
        mq = pymq.PyMedQuery()
        blob = mq.extract(
            get_all=False,
            sql_file_path=config.SQL_FILE_PATH_MODELS_WEIGHTS,
            image_extraction=False,
            format_params=format_params,
        )

        if mq.crud.self.log.error_config.logger:
            raise ValueError(f'extraction failed with: {mq.crud.self.log.error_config.logger}')

        self.log.info("Get meta data and decompress the model.")
        meta = blob[1]
        model_id = meta.get("model_id")[0]
        model_type = meta.get("model_type")[0]

        encoded_model = blob[0]
        weights = decode_weights(encoded_model)
        model = self.__load_weights(weights=weights, meta=meta)
        self.log.success(f"Model loaded: model_id = {model_id}")
        return model, model_id, model_type

    @timer
    def init_model_from_mq(self):
        """init_model_from_mq

        This method is called when the central processing is needed. It calls the
        appropriate functions of the central processing model.

        Parameters
        ------------
        None

        Returns
        ------------
        None
        """
        self.model, self.model_id, self.model_type = self.__get_model_from_mq()
    
    def __load_weights(self, weights: Dict[str, any], meta: Dict[str, str]):
        """Load weights for the model"""
        try:
            model = cpr.CentralProcessing(preproc = False).load_from_checkpoint(weights)
            model = model.to(self.device)
            model.eval()
            return model
        except (ValueError, TypeError) as e:
            self.log.error(f"I tried initiating the model: {meta} but failed with: {e}")


    def start_processing(self, model: nn.Module, x_stream: Dict[str, np.ndarray], extras: Dict[str, Any]) -> Dict[str, np.ndarray]:        
        """start_processing
        
        This method is called when the central processing is needed. It calls the
        appropriate functions of the central processing model.

        Parameters
        ------------
        model:nn.Module
            The central processing model.
        x_stream:Dict[str, np.ndarray]
            The input data. This data must have "x" as key.
        extras:Dict[str, Any]
            The extra data.

        Important
        ------------
        Extras dictionary is something the researchers need to define. There has to be a proper explanation of what the extras dictionary is and what it contains.
            Example of extras and input data:
                extras = {"resolution": [1,1,1]}
                x_stream = {"x": np.random.randn(32, 64, 64)}

        Returns
        ------------
        postproc:Dict[str, np.ndarray]
            The output data.
        """
        ################
        self.log.info("Start processing.")
        preproc = model.preprocess(data=x_stream, stage="predict", extras=extras)
        predict = model.predict_step(preproc)
        postproc = model.postprocess(predict, stage="predict", extras=extras)
        return postproc
    
    # def start_finetuning(self, model:pl.LightningModule) -> NoReturn:
    #     """start_finetuning
        
    #     This method is called when the central processing is needed. It calls the
    #     appropriate functions of the central processing model.

    #     Parameters
    #     ----------
    #     model:pl.LightningModule
    #         The central processing model.

    #     Returns
    #     -------
    #     None
    #     """
        # self.log.info("Start finetuning.")
        # trainer = pl.Trainer()
        # callbacks = [FinetuningScheduler()]
        # trainer = pl.Trainer(callbacks=callbacks)
        # data = DataModule()
        # trainer.fit(model, data)




