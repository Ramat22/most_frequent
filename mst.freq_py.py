# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 22:55:25 2021

@author: win10
"""

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('mississippi'))