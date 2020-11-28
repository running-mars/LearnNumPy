#-*- coding: UTF-8 -*-
# some arithmetic functions in numpy
# Ruunning Mars, guanzhengcn@foxmail.com
# 2020.11.28.23.59

import numpy as np

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
y = np.array([[9, 10, 11, 12], [13, 14, 15,16]])
print("x: \n", x)
print("y: \n", y)

print("add: \n", np.add(x, y))
print("remainder: \n", np.remainder(y, x))
print("x**2: \n", x**2)
print("y-x: \n", y-x)
print("x<5: \n", x<5)
print("x*y: \n", x*y)
print("matrix dot product: \n", np.dot(x, y.transpose()))