#-*- coding: UTF-8 -*-
# create an numpy array 
# Ruunning Mars, guanzhengcn@foxmail.com
# 2020.11.26.19.39

import numpy as np

array_1d = np.array([1, 2, 3, 1, 5])                        # create an array of rank 1
array_2d = np.array([[2, 3, 5], [1, 2, 4]])                 # create an array of rank 2
array_3d = np.array([[[1, 2], [3, 4]], [[1, 3], [3, 4]]])   # create an array of rank 3
print(array_1d, array_1d.size)          # size is the number of the elements in the array
print(array_2d, array_2d.ndim)          # ndim is the rank of the array
print(array_3d, array_3d.shape)         # shape means how many rows, columns, ..., the array has

print(type(array_3d))       # take a look at the type of the array

print(array_3d[0][1][0])       # access one elements in the array
