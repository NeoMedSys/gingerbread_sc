import os, sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/..")

import central_processing
import data_download
import cli_main


class Test_General:

    def test_imports(self):
        assert central_processing
        assert data_download
        assert cli_main

    def test_central_processing(self):
        pass
        # cpp = central_processing.CentralProcessing()
        # mock_data = np.random.randn(10, 10, 10)  # Please make sure this data mimics your own data
        # cpp.test_structure(data=mock_data)
        # cpp.load_state_dict(state_dict={'kdwkamd',
        #                                 2381232103})  # Anything should work as the function is mocked
