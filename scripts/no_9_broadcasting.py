#-*- coding: UTF-8 -*-
# some time using broadcasting
# Ruunning Mars, guanzhengcn@foxmail.com
# 2020.11.29.00.40

import numpy as np 
one_d = np.array([10])
two_d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
three_d = np.ones((3, 2))

print(np.add(two_d, one_d))
print(np.add(one_d, three_d))
print(np.add(two_d, three_d))   # run into some error