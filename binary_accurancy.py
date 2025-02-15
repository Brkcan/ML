#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 00:40:21 2025

@author: burakcan
"""

import tensorflow as tf
from tensorflow.keras.metrics import binary_accuracy
import numpy as np


y = np.array([1, 0, 1, 1, 0])
y_hat = np.array([0.90, 0.7, 0.6, 0.9, 0.6])


resultBinary = tf.convert_to_tensor(binary_accuracy(y, y_hat))

print(resultBinary)







