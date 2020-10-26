# This code is modified from https://github.com/facebookresearch/low-shot-shrink-hallucinate

import torch
import torch.nn as nn
import math
import torch.nn.functional as F
from torch.nn.utils import weight_norm

# --- gaussian initialize ---
def init_layer(L):
  # Initialization using fan-in
  if isinstance(L, nn.Conv2d):
    n = L.kernel_size[0]*L.kernel_size[1]*L.out_channels
    L.weight.data.normal_(0,math.sqrt(2.0/float(n)))
  elif isinstance(L, nn.BatchNorm2d):
    L.weight.data.fill_(1)
    L.bias.data.fill_(0)

class Flatten(nn.Module):
    def __init__(self):
        super(Flatten, self).__init__()
    
    def forward(self, x):
        return x.view(x.size(0), -1)

# 卷积网络Template
class ConvNet(nn.Module):
    def __init__(self,depth, flatten = True):
        super(ConvNet,self).__init__()
        self.grads = []
        self.fmaps = []
        trunk = []
        for i in range(depth):


#  1维卷积块
class Conv1DBlock(nn.Module):
    maml = False
    def __init_(self, indim, outdim, pool = True, padding = 1):
        super(ConvBlock, self).__init__()
        self.indim = indim
        self.outdim = outdim
    if self.maml:
    
    else:
        self.C = nn.Conv1d(indim, outdim ,1 ,padding=padding)
        self.BN = nn.BatchNorm1d(outdim)
    self.relu = nn.ReLU(inplace=True)

    self.parametrized_layers = [self.C, self.BN, self.relu]

    if pool:
        self.pool = nn.MaxPool1d(2)
        self.parametrized_layers.append(self.pool)
    
    for layer in self.parametrized_layers:
        init_layer(layer)
    self.trunk = nn.Sequential(*self.parametrized_layers)

    