import torch
import monai

class LitLRScheduler(torch.optim.lr_scheduler.CosineAnnealingLR):
    def step(self):
        print("⚡", "using LitLRScheduler", "⚡")
        super().step()

class LitWarmupCosineSchedule(monai.optimizers.lr_scheduler.WarmupCosineSchedule):
    def step(self):
        print("⚡", "using LitWarmupCosineSchedule", "⚡")
        super().step()