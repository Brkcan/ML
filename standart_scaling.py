#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:23:47 2025

@author: burakcan
"""

import numpy as np

data= np.array([4, 7, 1, 90, 45, 70, 23, 12, 6, 9, 45, 82, 65])
mean = np.mean(data)
std = np.std(data)
print(f'Mean: {mean}, Standard Deviation: {std}')

result = (data - mean) / std

print(f'Data: {data}')
print(f'Scaled Data: {result}')

print('--------------------------------')