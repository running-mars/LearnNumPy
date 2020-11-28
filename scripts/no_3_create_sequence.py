#-*- coding: UTF-8 -*-
# create a sequence using numpy
# Ruunning Mars, guanzhengcn@foxmail.com
# 2020.11.28.23.30

import numpy as np

a = np.arange(0, 10, 2)     # from 0 to 10, step is 2
print(a)

b = np.arange(6)            # from 0 to 6, step is 1
print(b)

c = np.linspace(0, 10, 6)   # from 0 to 6, generate 6 numbers evenly spaced
print(c)