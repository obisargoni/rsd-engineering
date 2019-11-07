# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:47:54 2019

@author: student
"""

# Write regression test for fractal tree

# Import data that is produced by fractal tree
from .fractal_tree import d, first_branch
import pickle

def test_fractal_tree():
    orig_d_path = "nFinal.data"
    with open(orig_d_path, "rb") as f:
        orig_d = pickle.load(f)
        assert orig_d == d