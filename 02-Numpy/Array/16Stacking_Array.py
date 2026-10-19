'''
means bahut sare arrays ko combine krna

vertically
horizontally

vstack() -- row wise
hstack() -- column wise
'''

import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.stack((arr1,arr2)))  # vertically stack
print(np.hstack((arr1,arr2))) # horizontally stack

