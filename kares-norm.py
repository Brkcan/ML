#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 13:02:20 2025

@author: burakcan
"""

import numpy as np

dataset = np.array([[1, 2, 3], [4, 5, 6], [3, 2, 7], [5, 9, 5]])
print(dataset)
from tensorflow.keras.layers import Normalization

norm_layer = Normalization()
norm_layer.adapt(dataset)

print(norm_layer.mean)
print(norm_layer.variance)