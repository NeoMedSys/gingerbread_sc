import torch


class MockModel(torch.nn.Module):

    def __init__(self, *args, **kwargs):
        super().__init__()

    def forward(self, x):
        return x

    def load_state_dict(self, state_dict, strict=True):
        pass