#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 15:15:45 2025

@author: burakcan
"""

import numpy as np
import matplotlib.pyplot as plt

def tanh(x):
    return (np.e ** (2 * x) - 1) / (np.e ** (2 * x) + 1)

x = np.linspace(-10, 10, 1000)
y = tanh(x)


plt.title('Tanj Function', fontsize=14, fontweight='bold', pad=20)
axis = plt.gca()

axis.spines['left'].set_position('center')
axis.spines['bottom'].set_position('center')
axis.spines['top'].set_color(None)
axis.spines['right'].set_color(None)

axis.set_ylim(-1, 1)
plt.plot(x, y, color='red')
plt.show()


