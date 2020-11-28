#-*- coding: UTF-8 -*-
# array slicing
# Ruunning Mars, guanzhengcn@foxmail.com
# 2020.11.28.23.44

import numpy as np

# sololearn: To slice an array, you indicate the start:stop:step of the subset in square brackets.
x = np.arange(8)     
print("x: ", x, x.shape)

y = x[0:4]      # if no step, step is 1
print("y: ", y, y.shape)

z = x[6:]       # if no end and no step, step is 1 and from 6th element to the end
print("z: ", z, z.shape)

z[1] = 100      # change the value of the slice, the original array is also changed, indeed, the same data
print("x: ", x)

a = np.array([[10, 11, 12, 13], [20, 22, 23, 25]])
print("a: ", a, a.shape)
print(a[0:1, 1])    # 0th row, 1st column
print(a[..., 1])    # all elements in the 1st dimension, 1st column
print(a[:, 3])      # all elements in the 1st simension, 3rd column