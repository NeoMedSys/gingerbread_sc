# global imports
from torch import Tensor
from torch.utils.data import DataLoader, Subset
from sklearn.model_selection import KFold
import numpy as np
import pytorch_lightning as pl
import coloredlogs, verboselogs
from typing import NoReturn

# local imports
import data_loader.data_handler as dh

class DataModule(pl.LightningDataModule):
    """
    DataModule for training, validation, and test dataloaders.

    Attributes:
    ----------
    fold: int
        The fold to be used for training.
    nfolds: int
        The number of folds to be used.
    batch_size: int
        The batch size to be used.


    Methods:
    -------
    """
    def __init__(self, 
                fold: int = 0, 
                nfolds: int = 5,
                batch_size: int = 1
                ) -> NoReturn:
        super().__init__()
        
        self.fold = fold
        self.nfolds = nfolds
        self.batch_size = batch_size

         # logger [color]
        coloredlogs.install()
        self.logga = verboselogs.VerboseLogger(__name__)
        self.logga.info("DataTemplate initialized")


    def setup(self, stage: str) -> NoReturn:
        """Split the dataset into train/val/test/predict datasets.
        
        Parameters:
        ----------
        stage: str
            The stage to be used for the setup.

        Returns:
        -------
        None
        """
        if stage == 'fit':
            # fitting setup
            self.random_full = dh.DataHandler(size = 32, length = 64 * 4)
            self.random_full.stage = "train"
            self.kf = KFold(n_splits=self.nfolds, shuffle=True)
            split = self.kf.split(np.arange(len(self.random_full)))
            
            for fold_num, (train_idx, val_idx) in enumerate(split):
                if fold_num == self.fold:
                    self.logga.info(f"Fold {fold_num} selected")
                    self.logga.info(f"Train: {len(train_idx)} Val: {len(val_idx)}")
                    break
            self.random_train = Subset(self.random_full, indices=train_idx)
            self.logga.info("Train dataset initialized")

        if stage in ("fit", "validate"):
            self.random_full.stage = "val"
            self.random_val = Subset(self.random_full, indices=val_idx)
            self.logga.info("Val dataset initialized")

        if stage == 'test':
            self.random_full.stage = 'test'
            self.random_test = Subset(self.random_full, indices=val_idx)
            self.logga.info("Test dataset initialized")

        if stage == 'predict':
            if self.predict_input is None:
                raise ValueError("predict_input must be provided for prediction. Make sure to add data with add_predict_data()")
            self.logga.info("using predict. Use add_predict_data() to add data.")

    def train_dataloader(self) -> DataLoader:
        return DataLoader(self.random_train, batch_size=self.batch_size)

    def val_dataloader(self) -> DataLoader:
        return DataLoader(self.random_val, batch_size=self.batch_size)

    def test_dataloader(self) -> DataLoader:
        return DataLoader(self.random_test, batch_size=1)
    
    def teardown(self, stage: str):
        """Clean-up after the run is finished.
        
        Parameters:
        ----------
        stage: str
            The stage to be used for the teardown.

        Returns:
        -------
        None
        """
        pass
    

    
    