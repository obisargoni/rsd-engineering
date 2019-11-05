# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:47:10 2019

@author: student
"""
import numpy as np
from pytest import raises

from .diffusion_model import energy
def test_energy_calculation():
  """ Optional description for nose reporting """
  # Test something
    
  assert energy(np.arange(5)) == 26
  assert energy(np.array([0]*5)) == 0
  assert energy(np.array([1]*5)) == 0
  assert energy(np.array([2]*5)) == 15

def test_energy_types():
  with raises(ValueError):
      energy(np.array([-1]))
  with raises(ValueError):
      energy(-3)
  with raises(ValueError):
      energy("string")