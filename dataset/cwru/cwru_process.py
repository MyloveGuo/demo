from scipy.io import loadmat
import os
from os import listdir
from os.path import isfile, isdir, join
import numpy as np

cwd = os.getcwd()
data_path = join(cwd,'source\cwru')
savedir = './'
dataset_list = ['base','val','novel']

folder_list = [f[:-4] for f in listdir(data_path) if isfile(join(data_path, f))]

# 类别字典
label_dict = dict(zip(folder_list,range(0,len(folder_list))))

# print(label_dict)
# 类别文件下所有数据
classfile_list_all = []

for i, folder in enumerate(folder_list):
    folder_path = join(data_path, folder)
    classfile_list_all.append( [ join(folder_path, cf) for cf in listdir(folder_path) if (isfile(join(folder_path,cf)) and cf[0] != '.')])
    random.shuffle(classfile_list_all[i])