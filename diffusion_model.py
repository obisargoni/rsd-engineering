# 1D diffusion model
import numpy as np

def energy(density, coeff=1.0):
  """ Energy associated with the diffusion model

      Parameters
      ----------

      density: array of positive integers
          Number of particles at each position i in the array
      coeff: float
          Diffusion coefficient.
  """
  # implementation goes here
  
  # Check input density type
  if isinstance(density, str):
      raise ValueError
  if isinstance(density, (list, tuple, np.ndarray)) == False:
      raise ValueError
  if (density < 0).any():
      raise ValueError
  
  # Caculate energy
  e = [(i+1)*coeff*max(0,j-1) for i,j in enumerate(density)]
  return sum(e)