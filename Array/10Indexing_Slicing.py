# Access
'''
array[index] #1d array
array[row, coloum] #2d

'''

import numpy as np

arr1 = np.array([10,20,30,40,50])
# print(arr[10])  -- index out of bound
print(arr1[3])
print(arr1[-1])  # last element




# Slicing
'''

array[start:stop:step]

'''
arr2 = np.array([10,20,30,40,50,60])
print("\n",arr2[1:5])  #index 1 to 4
print(arr2[:4])   #index 0 to 3
print(arr2[::2])  #every second element
print(arr2[::-1]) #reverse array
