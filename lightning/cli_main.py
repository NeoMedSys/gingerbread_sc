# global imports
from pytorch_lightning.cli import LightningCLI
from pytorch_lightning.callbacks import EarlyStopping
import monai.optimizers.lr_scheduler
import central_processing as cpr
import torch

# local imports
import central_processing as cpr
from data_loader.data_module import DataModule


class CustomLightningCLI(LightningCLI):
    """Custom LightningCLI to add extra callbacks and params
    If you want to add extra function to the CLI, you can do it here.
    See: https://pytorch-lightning.readthedocs.io/en/stable/cli/lightning_cli.html for more info.

    Attributes
    ----------
    None

    Methods
    -------
    
    """
    def add_arguments_to_parser(self, parser: LightningCLI) -> None:
        """
        Add extra callbacks and params to the parser
        Any callbacks added here will replace the functions in the CentralProcessing class.
        f.eks. By having "add_opimizer_args" here, the optimizer in the CentralProcessing class will be replaced by the optimizer in this function.
        """


        # Add extra callbacks
        parser.add_lightning_class_args(EarlyStopping, "my_early_stopping")
        # set default values to the callbacks
        parser.set_defaults({"my_early_stopping.monitor": "val_metric", "my_early_stopping.patience": 5})
        
        # # ## Add extra params
        parser.add_optimizer_args(torch.optim.Adam)
        parser.add_lr_scheduler_args(monai.optimizers.lr_scheduler.WarmupCosineSchedule)
        parser.set_defaults({"optimizer.lr": 1})
        parser.set_defaults({"lr_scheduler.warmup_steps": 250, "lr_scheduler.t_total": 1000})


        # You can also link params together
        parser.link_arguments("data.batch_size", "model.sw_batch_size")


    def before_fit(self):
        # can access params via self.config_init.[type,ie train, val, etc].someparam
        pass

    def after_fit(self):
        pass

    def before_validate(self):
        pass

    def after_validate(self):
        pass

def cli_main():
    cli = CustomLightningCLI(cpr.CentralProcessing, DataModule, seed_everything_default=31345123)

if __name__ == "__main__":
    cli_main()
