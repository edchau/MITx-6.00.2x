#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 13:31:28 2018

@author: Edward
"""
import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    if numTrials < 1:
        raise ValueError("Must be greater than 0")
    count = 0
    for trial in range(numTrials):
        bucket = ["R", "R", "R", "G", "G", "G"]
        drawings = []
        for draw in range(3):
            choose = random.choice(bucket)
            drawings.append(choose)
            bucket.remove(choose)
        
        if all(drawings[0] == others for others in drawings):
            count += 1
        
    return count / numTrials
