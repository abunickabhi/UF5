# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 12:59:48 2020

@author: abhij
"""

import collections
print([item for item, count in collections.Counter(quadtxt).items() if count > 1])
