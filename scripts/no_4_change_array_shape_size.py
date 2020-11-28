#-*- coding: UTF-8 -*-
# change array's shape and size
# Ruunning Mars, guanzhengcn@foxmail.com
# 2020.11.28.23.36

import numpy as np

a = np.arange(10)           # generate a sequence(1d array)
print(a, a.shape, type(a))

a.resize(2, 5)              # modify shape of a
print(a, a.shape)

b = np.array([[1, 2, 3], [4, 5, 6]])    # generate a 2d array
print(b, b.shape, type(b))

print(b.reshape(3, 2))      # reshape returns a new array, but b is not changed
print(b)

print(b.ravel())            # reval returns a new flattened array, but b is not changed
print(b)

print(b.transpose())        # transpose also does not modify b
print(b)
