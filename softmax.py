#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 15:47:40 2025

@author: burakcan
"""

"""
Softmax fonksiyonu çok sınıflı sınıflandırma 
    problemlerinde çıktı katmanlarında kullanılmaktadır.
"""

import numpy as np
x = np.array([3, 6, 4, 1, 7])
sm = np.e ** x / np.sum(np.e ** x)

print(np.sum(sm))


