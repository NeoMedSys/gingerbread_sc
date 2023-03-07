"""
This is script for custom exceptions
"""


class CentralProcessingInitModelsError(Exception):
    """Fail to init models in centralProcessing"""


class CentralProcessingPreprocessImageError(Exception):
    """Fail to preprocess image in centralProcessing"""


class CentralProcessingPredictImageError(Exception):
    """Fail to predict image in centralProcessing"""


class CentralProcessingPostprocessImageError(Exception):
    """Fail to postprocess image in centralProcessing"""


class CentralProcessingProcessImageError(Exception):
    """Fail to process image in centralProcessing"""


class DatabaseUploadError(Exception):
    """Fail to upload data to MQ db"""


class DatabaseLoadError(Exception):
    """Fail to load data from MQ db"""


class DatabasePrepareRecordError(Exception):
    """Fail to prepare record for a table in MQ db"""


class RealtimeProcessError(Exception):
    """Fail to process realtime request"""