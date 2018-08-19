#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 21:33:17 2018

@author: Edward
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    
    lengths = [len(string) for string in L] 

    mean = sum(lengths)/float(len(lengths))
    tot = 0.0
    for x in lengths:
        tot += (x - mean)**2
    std = (tot/len(lengths))**0.5
    return std