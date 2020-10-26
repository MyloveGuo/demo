import torch.nn as nn
import numpy as np
from abc import abstractclassmethod
from tensorboardX import SummaryWriter

"""
模型通用模板 -- 包含通用方法，forward抽象方法
"""
class MetaTemplate(nn.Module):
    def __init__(self):

    @abstractclassmethod
    def set_forward(self,x,is_feature):
        pass
    
    @abstractclassmethod
    def set_forward_loss(self,x):
        pass
    
    # 模型准确率计算
    def correct(self,x):

    # 模型训练操作
    def train_loop(self):

    # 模型测试操作
    def test_loop(self):
    
    