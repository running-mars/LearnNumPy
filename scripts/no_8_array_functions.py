#-*- coding: UTF-8 -*-
# some array functions
# Ruunning Mars, guanzhengcn@foxmail.com
# 2020.11.29.00.28

import numpy as np

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
y = np.array([[9, 10, 11, 12], [13, 14, 15, 16]])
print("x: \n", x)
print("y: \n", y)

print(x.sum(axis=0))        # 0 for row sum, returns many columns
print(x.sum(axis=1))        # 1 for column sum, returns many rows
print(np.min(x))            # minimum of x
print(x.min())
print(x.max(axis=1))        # return the maximum of columns
print(np.cumsum(y))         # row by row
print(np.corrcoef(y))       # correlation coefficient
print(y.std())              # standard deviation