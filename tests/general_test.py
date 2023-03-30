import pytest
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
        central_processing.CentralProcessing()
