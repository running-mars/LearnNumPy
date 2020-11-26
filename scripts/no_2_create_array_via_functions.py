#-*- coding: UTF-8 -*-
# create an numpy array 
# Ruunning Mars, guanzhengcn@foxmail.com
# 2020.11.26.19.39

import numpy as np

a = np.ones((3, 2))         # 3x2 array with elements all 1
print(a)

b = np.zeros((3, 4))        # 3x4 array with elements all 0
print(b)

c = np.random.random(3)     # 3x1 array with elements random values 
print(c)

d = np.full((2, 2), 12)     # 2x2 array filled with constant value 12
print(d)

e = np.empty((2, 3))        # 2x3 array with value uninitialized
print(e)

f = np.eye(3, 4)            # 3x4 eye matrix 
print(f)

g = np.identity(3)          # a square matrix with ones on the main diagonal
print(g)

h = np.identity(3, dtype=bool)  # dtype is used to specify the data type
print(h)

i = np.full((2, 2), 3, dtype=np.float32)
print(i)

j = b.copy()                # create a copy
print(j)

k = np.loadtxt("../data/array_0.txt")   # load data from txt file
print(k)

np.save("../data/array_i", i)           # saved to npy file
new_i = np.load("../data/array_i.npy")
print(new_i)
