#flattering array
#1. ravel()
#2. flatter()
# ----- used when we reshape multidimension array into 1D array


'''
.ravel() --> view
.flatten() --> copy    #  diff bw ravel and flatten 
'''

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr.ravel())
print(arr.flatten())
