import os, sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')

import central_processing
import data_download
import numpy as np
from config.model_conf import MODELS


class Test_General:

    def test_imports(self):
        assert central_processing
        assert data_download

    def test_central_processing(self):
        for model_key in MODELS.keys():
            model = MODELS[model_key]
            cpp = central_processing.CentralProcessing()
            preprocessed_data = cpp.preprocess(data=cpp.test_data)
            assert isinstance(preprocessed_data, np.ndarray)
            processed_data = cpp.predict_step(data=preprocessed_data, model=model)
            assert isinstance(processed_data, np.ndarray)
            postprocessed_data = cpp.postprocess(data=processed_data)
            assert isinstance(postprocessed_data, np.ndarray)
