#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
def total_value_mass(packing, values, mass, max_size):
  v = 0.0  
  s = 0.0 
  n = len(packing)
  for i in range(n):
   if packing[i] == 1:
      v += values[i]
      s += mass[i]
   if s > max_size:
      v = 0.0
  return (v, s)
def adjacent(packing, rnd):
  n = len(packing)
  result = np.copy(packing)
  i = rnd.randint(n)
  if result[i] == 0:
    result[i] = 1
  elif result[i] == 1:
    result[i] = 0
  return result
def solve(n_items, rnd, values, mass, max_size,   max_iter, start_temperature, alpha):
  curr_temperature = start_temperature
  curr_packing = np.ones(n_items, dtype=np.int64)
  print("Initial guess: ")
  print(curr_packing)
  (curr_valu, curr_size) =     total_value_mass(curr_packing, values, mass, max_size)
  iteration = 0
  interval = (int)(max_iter / 10)
  while iteration < max_iter:
    adj_packing = adjacent(curr_packing, rnd)
    (adj_v, _) = total_value_mass(adj_packing,       values, mass, max_size)
    if adj_v > curr_valu: 
      curr_packing = adj_packing; curr_valu = adj_v
    else:          
      accept_p =         np.exp( (adj_v - curr_valu ) / curr_temperature ) 
      p = rnd.random()
      if p < accept_p: 
        curr_packing = adj_packing; curr_valu = adj_v   
    if iteration % interval == 0:
      print("iter = %6d : curr value = %7.0f :         curr temp = %10.2f "         % (iteration, curr_valu, curr_temperature))
    if curr_temperature < 0.00001:
      curr_temperature = 0.00001
    else:
      curr_temperature *= alpha
    iteration += 1
  return curr_packing       
def main():
  print("\nBegin knapsack simulated annealing")
  print("Our objective is to maximize value    and minimize mass")
  values = np.array([1, 2, 5, 10, 0.5, 0.3, 1.6, 4, 2, 1.9])
  mass = np.array([1, 0.2, 0.5, 2, 0.1, 0.5, 10, 2, 6, 1])
  max_mass = 25
  print("\nItem values: ")
  print(values)
  print("\nItem mass: ")
  print(mass)
  print("\nMax total mass = %d " % max_mass)
  rnd = np.random.RandomState(5)
  max_iter = 1000
  start_temperature = 10000.0
  alpha = 0.98
  print("\nSettings: ")
  print("max_iter = %d " % max_iter)
  print("start_temperature = %0.1f "     % start_temperature)
  print("alpha = %0.2f " % alpha)
  print("\nStarting solve() ")
  packing = solve(10, rnd, values, mass, 
    max_mass, max_iter, start_temperature, alpha)
  print("Finished solve() ")
  print("\nBest packing found: ")
  print(packing)
  (v,s) =     total_value_mass(packing, values, mass, max_mass)
  print("\nTotal values of packing = %0.1f " % v)
  print("Total mass  of packing = %0.1f " % s)
  print("\nEnd")
if __name__ == "__main__":
  main()


# In[ ]:




