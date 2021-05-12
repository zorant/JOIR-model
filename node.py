#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 13:57:42 2018

@author: zoran
"""

import numpy as np
from support import Support

class Node:
    
    def __init__(self, name, tstr_min=0.1, tstr_max=2, buff_len=70, k=10, dt=0.001, g=1, Nt=2000):
        self.name = name
        self.support = Support(tstr_min, tstr_max, buff_len, k, dt, g, Nt)
        self.value = np.zeros(Nt) 