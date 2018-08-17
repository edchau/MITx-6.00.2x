#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 15:49:51 2018

@author: Edward
"""

import random

def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    return random.choice(range(0, 101, 2))
    
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 10

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.choice(range(10, 21, 2)) #use randrange(0, 21, 2)