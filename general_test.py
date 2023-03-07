
import pytest
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__))) 

import central_processing
import data_download
import cli_main
import data_loader.data_handling

class Test_General:

    def test_imports(self):
        assert central_processing
        assert data_download
        assert cli_main
        assert data_loader.data_handling
    
    def test_data_handling(self):
        test_data_module = data_loader.data_handling.DataHandler()
        test_data_module.add_data({"x": 1, "y": 2})

