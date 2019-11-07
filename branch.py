# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:53:45 2019

@author: student
"""
from math import sin, cos

class Branch:
    def __init__(self, start_coord, length, angle):
        self.sc = start_coord
        self.l = length
        self.a = angle
        
        # Generate end coordinate
        self.ec = [self.sc[0] + self.l*sin(self.a), self.sc[1] + self.l*cos(self.a)]
    
    def getAngle(self):
        return self.a
    def getLength(self):
        return self.l
    def getEndCoord(self):
        return self.ec
    