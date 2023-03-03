from typing import Dict, List, Optional, Tuple, Union, Any, cast, NoReturn
import monai
import torch
from torch import Tensor
import pytorch_lightning as pl
import wandb
import numpy as np
from pytorch_lightning.loggers import WandbLogger
from monai.optimizers.lr_scheduler import WarmupCosineSchedule
import coloredlogs, verboselogs
from monai.transforms import (
    AddChanneld,
    ScaleIntensityd,
    ToTensord,
)

import config.config as cfg


class CentralProcessing(pl.LightningModule):
    """
    CentralProcessing for training, validation, and test dataloaders.
    This includes the model, loss function, optimizer, and scheduler and all other model workflow.

    Attributes
    ----------
    preproc: bool
        Whether to use preprocessing.
    use_wandb: bool
        Whether to use wandb logger.
    wandb_project_name: str
        Name of the wandb project.
    wandb_entity: str
        Name of the wandb entity.
    in_features: int
        Number of input features.
    out_features: int
        Number of output features.
    patch_size: Union[Tuple, int]
        Size of the patch to be used for inference.
    overlap: Union[int, float]
        Overlap of the patches.
    mode: str
        Mode of the patches.
    sw_batch_size: int
        Batch size of the patches.
    learning_rate: float
        Learning rate of the model.

    Returns
    -------
    None
    
    Attention
    ---------
    This class is a subclass of `pytorch_lightning.LightningModule`.

    
    """
    def __init__(self,
                preproc: bool = True,
                use_wandb: bool = False,
                wandb_project_name: Optional[str] = None,
                wandb_entity: Optional[str] = None,
                in_features: int = 1, 
                out_features: int = 1,
                patch_size: Union[Tuple, int] = (16, 16),
                overlap: Union[int, float] = 0.5,
                inferer_mode: str = "gaussian",
                sw_batch_size: int = 1,
                learning_rate: float = 4e-4
                ) -> NoReturn:

        super().__init__()

        # logger [color]
        coloredlogs.install()
        self.logga = verboselogs.VerboseLogger(__name__)
        self.logga.info("Model initialized")

        try:
            self.save_hyperparameters() # This will save the model params to the checkpoint and use self.hparams to access them
            
            # wandb
            if self.hparams.use_wandb:
                wandb.init(project=self.hparams.project_name, entity=self.hparams.entity)
                self.logwd = WandbLogger(
                                        project=self.hparams.project_name, 
                                        entity=self.hparams.entity
                                        )

            # MODEL
            self.model = torch.nn.LazyConv2d(
                                            out_channels=self.hparams.out_features, 
                                            kernel_size=3, 
                                            padding=1
                                            )
            
            # inferers
            self.infer = monai.inferers.SlidingWindowInferer(
                                                            roi_size=self.hparams.patch_size,
                                                            sw_batch_size=self.hparams.sw_batch_size, 
                                                            overlap=self.hparams.overlap, 
                                                            mode=self.hparams.inferer_mode
                                                            )
        
        except Exception as e:
            self.logga.error(f"Error in __init__: {e}")

    def forward(self, x: Tensor) -> Tensor:
        """
        Forward pass of the model.
        
        Parameters
        ----------
        x: Tensor
            Input tensor.

        Returns
        -------
        x: Tensor
            Output tensor.
        """
        try:
            x = self.model(x)
            return x
        except Exception as e:
            self.logga.error(f"Error in forward: {e}")

    def loss(self, preds: Tensor, labels: Tensor) -> Tensor:
        """
        Loss function.
        
        Parameters
        ----------
        preds: Tensor
            Predictions.
        labels: Tensor
            Labels.

        Returns
        -------
        loss: Tensor
            Loss.
        """
        try:
            # An arbitrary loss to have a loss that updates the model weights during `Trainer.fit` calls
            loss = torch.nn.functional.mse_loss(preds, labels)
            return loss
        except Exception as e:
            self.logga.error(f"Error in loss: {e}")

    def step(self, batch: Tensor) -> Tensor:
        """
        Step function.

        Parameters
        ----------
        batch: Tensor
            Batch.

        Returns
        -------
        y_pred: Tensor
            Predictions.
        """
        try:
            # y_pred, y = self(batch["x"]), batch["y"]
            y_pred = self.infer(batch["x"], self.model)
            # y = batch["y"]
            # loss = self.loss(y_pred, y)
            return y_pred
        except Exception as e:
            self.logga.error(f"Error in step: {e}")
        
    def metrics(self, y_pred: Tensor, y: Tensor) -> Dict[str, Tensor]:
        """
        Metrics function.

        Parameters
        ----------
        y_pred: Tensor
            Predictions.
        y: Tensor
            Labels.

        Returns
        -------
        metrics: Dict[str, Tensor]
            Metrics.
        """
        try:
            # An arbitrary metric to to monitor during `Trainer.fit` calls
            return torch.nn.functional.mse_loss(y_pred, y)
        except Exception as e:
            self.logga.error(f"Error in metrics: {e}")

    def training_step(self, batch: Tensor, batch_idx: int) -> Dict[str, Tensor]:
        """
        Training step function.

        Parameters
        ----------
        batch: Tensor
            Batch.
        batch_idx: int
            Batch index.

        Returns
        -------
        loss: Tensor
            Loss.
        """
        try:
            if self.hparams.preproc:
                batch = self.preprocess(batch, stage="train") # preprocess the batch
            y_pred = self.step(batch)
            loss = self.loss(y_pred, batch["y"])
            if self.hparams.use_wandb:
                self.logwd.log_metrics({"train_batch_loss": loss.item()})
            self.log("train_batch_loss", loss)
            return {"loss": loss}
        except Exception as e:
            self.logga.error(f"Error in training_step: {e}")

    def training_step_end(self, training_step_outputs: Dict[str, Tensor]) -> Dict[str, Tensor]:
        """
        Training step end function.
        
        Parameters
        ----------
        training_step_outputs: Dict[str, Tensor]
            Training step outputs.
            
        Returns
        -------
        training_step_outputs: Dict[str, Tensor]
            Training step outputs.
        """
        try:
            return training_step_outputs
        except Exception as e:
            self.logga.error(f"Error in training_step_end: {e}")

    def training_epoch_end(self, outputs: Dict[str, Tensor]) -> NoReturn:
        """
        Training epoch end function.
        
        Parameters
        ----------
        outputs: Dict[str, Tensor]
            Outputs.
            
        Returns
        -------
        None
        """
        try:
            outputs = cast(List[Dict[str, Tensor]], outputs)
            torch.stack([x["loss"] for x in outputs]).mean()
            end_loss = torch.stack([x["loss"] for x in outputs]).mean()
            self.log("train_loss", end_loss)
        except Exception as e:
            self.logga.error("Error in training_epoch_end: {}".format(e))

    def validation_step(self, batch: Tensor, batch_idx: int) -> Dict[str, Tensor]:
        """
        Validation step function.

        Parameters
        ----------
        batch: Tensor
            Batch.
        batch_idx: int
            Batch index.

        Returns
        -------
        val_metric: Tensor
            Validation metric.
        val_loss: Tensor
            Validation loss.
        """
        try:
            batch = self.preprocess(batch, stage="val") # preprocess the batch
            y_pred = self.step(batch)
            metric = self.metrics(y_pred, batch["y"])
            loss = self.loss(y_pred, batch["y"])

            if self.hparams.use_wandb:
                self.logwd.log_metrics({"val_batch_val_metric": metric.item()})
                self.logwd.log_metrics({"val_batch_val_loss": loss.item()})
            self.log("val_batch_val_metric", metric)
            self.log("val_batch_loss", loss)
            return {"val_metric": metric, "val_loss": loss} # you can add more if you want, what you want to monitor can be added in the i.e EarlyStopping callback or other callbacks. 
        except Exception as e:
            self.logga.error(f"Could not validate in validation_step: {e}")

    def validation_epoch_end(self, outputs: Union[Dict[str, Dict[str, Tensor]], List[Dict[str, Tensor]]]) -> NoReturn:
        """
        Validation epoch end function.

        Parameters
        ----------
        outputs: Union[Dict[str, Dict[str, Tensor]], List[Dict[str, Tensor]]]
            Outputs.

        Returns
        -------
        None
        """
        try:
            outputs = cast(List[Dict[str, Tensor]], outputs)
            end_metric = torch.stack([x["val_metric"] for x in outputs]).mean()
            self.log("val_metric", end_metric)
        except Exception as e:
            self.logga.error(f"Could not validate in validation_epoch_end: {e}")

    def test_step(self, batch: Tensor, batch_idx: int) -> Dict[str, List[Tensor]]:
        """
        Test step function.
        
        Parameters
        ----------
        batch: Tensor
            Batch.
            batch_idx: int
            Batch index.
            
        Returns
        -------
        y_pred: List[Tensor]
            Predictions.
        """
        try:
            batch = self.preprocess(batch, stage="test") # preprocess the batch
            y_pred = self.step(batch["x"])
            metric = self.metrics(y_pred, batch["y"])
            return {"y_pred": metric}
        except Exception as e:
            self.logga.error(f"Could not test in test_step: {e}")

    def test_epoch_end(self, outputs: Union[Dict[str, Dict[str, Tensor]], List[Dict[str, Tensor]]]) -> NoReturn:
        """
        Test epoch end function.

        Parameters
        ----------
        outputs: Union[Dict[str, Dict[str, Tensor]], List[Dict[str, Tensor]]]
            Outputs.

        Returns
        -------
        None
        """
        try:
            outputs = cast(List[Dict[str, Tensor]], outputs)
            torch.stack([x["loss"] for x in outputs]).mean()
        except Exception as e:
            self.logga.error(f"Could not test in test_epoch_end: {e}")

    def predict_step(self, batch: Tensor, batch_idx: Optional[int] = None, dataloader_idx: Optional[int] = None) -> Dict[str, Tensor]:
        """
        Predict step function.

        Parameters
        ----------
        batch: Tensor
            Batch.
        batch_idx: int
            Batch index.
        dataloader_idx: int
            Dataloader index.

        Returns
        -------
        y_pred: Tensor
            Predictions.
        """
        try:
            self.eval()
            with torch.no_grad():
                y_pred = self.infer(batch["x"], self.model)
            return {"y_pred": y_pred}
        except Exception as e:
            self.logga.error(f"Could not predict: {e}")
    
    def configure_optimizers(self):
        """
        Configure optimizers function.

        Returns
        -------
        optimizer: torch.optim.Optimizer
            Optimizer.
        """
        try:
            optimizer = {
                "sgd": torch.optim.SGD(self.parameters(), lr=self.learning_rate, momentum=0.9, weight_decay=self.args.weight_decay),
                "adam": torch.optim.Adam(self.parameters(), lr=self.learning_rate, weight_decay=self.args.weight_decay),
            }[self.args.optimizer.lower()]

            if self.args.scheduler:
                scheduler = {
                    "scheduler": WarmupCosineSchedule(
                        optimizer=optimizer,
                        warmup_steps=250,
                        t_total=self.args.epochs * len(self.trainer.datamodule.train_dataloader()),
                    ),
                    "interval": "step",
                    "frequency": 1,
                }
                return {"optimizer": optimizer, "monitor": "val_metric", "lr_scheduler": scheduler}
            return {"optimizer": optimizer, "monitor": "val_metric"}
        except Exception as e:
            self.logga.warning(f"Could not configure optimizers: {e}")

    def postprocess(self, data: Dict[str, np.ndarray], stage:str, extras:Dict[str,Any] = {}) -> Tensor:
        """Postprocess the data after training/val/test/predict
        
        Parameters
        ----------
        data : dict
            the data to be postprocessed
        stage : str
            the stage of the postprocessing, e.g. "train", "val", "test", "predict"
        extras: dict
            additional arguments for preprocessing such as resolution information etc. 
            If provided, explain in depth in the docstring of the input and the input type.
            Example of extras:
                resolution [list]: resolution of the image, e.g. {"resolution": [1.0, 1.0, 1.0]
        Returns
        -------
        Tensor
            the postprocessed data
        """
        resolution = extras.get("resolution", None)
        self.logga.info(f"Postprocessing data for stage {stage}")
        try:
            # Fill here
            pass
        except Exception as e:
            self.logga.error(f"Postprocessing failed for stage {stage} with error {e}")
        return data

    def preprocess(self, data: Dict[str, Tensor], stage:str, extras:Dict[str, Any] = {}) -> dict:
        """Preprocess the data before training/val/test/predict
        
        Parameters
        ----------
        data : dict
            the data to be preprocessed
        stage : str
            the stage of the preprocessing, e.g. "train", "val", "test", "predict"
        extras: dict
            additional arguments for preprocessing such as resolution information etc.
            If provided, explain in depth in the docstring of the input and the input type.
            Example of extras:
                resolution [list]: resolution of the image, e.g. {"resolution": [1.0, 1.0, 1.0]
        Returns
        -------
        dict
            the preprocessed data
        """
        resolution = extras.get("resolution", None)

        self.logga.info(f"Preprocessing data for stage {stage}")
        try:
            if not all(stage in cfg.STAGES for s in cfg.STAGES):
                self.logga.warning(f"stage must be one of {cfg.STAGES}, got {stage}")
                raise ValueError(f"stage must be one of {cfg.STAGES}, got {stage}")
    
            if stage == "predict":
                data = AddChanneld(keys="x")(data)
                data = ScaleIntensityd(keys="x", channel_wise=True)(data)
                data = ToTensord(keys="x", dtype=torch.float32)(data)
            
            else:
                #data =LoadImaged(keys=["x", "y"])
                data = AddChanneld(keys=["x", "y"])(data)
                data = ScaleIntensityd(keys="x", channel_wise=True)(data)
                data = ToTensord(keys=["x", "y"], dtype=torch.float32)(data)
            return data
        except Exception as e:
            self.logga.error(f"Postprocessing failed for stage {stage} with error {e}")