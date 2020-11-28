#-*- coding: UTF-8 -*-
# some elementwise functions
# Ruunning Mars, guanzhengcn@foxmail.com
# 2020.11.29.00.17

import numpy as np

x = np.array([[1.2, 2.6], [3.0, 4.9]])
print("x: \n", x)

print(np.exp(x))    # calculate exponetial of each element
print(np.sqrt(x))   # calculate square root of each element
print(np.round(x))  # returns the array rounded to the optionally specified numdber of decimal places
print(np.trunc(x))  # returns the array with truncated elements
print(np.floor(x))  # returns the greatest integer less than or equal to the value
print(np.ceil(x))   # returns the smallest integer greater than or equalto the value
print(np.log(x))    # returns the natural logarithm for each elements

# ...