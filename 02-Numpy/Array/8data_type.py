# -- give information of data type   (dtype)

import numpy as np
arr = np.array([[1,2,3],[6,5,4]])
print(arr.dtype)




# -- Change Data Type
# array.astype(new type)
arr1 = np.array([1.1,2.5,3.4,4.0])
print(arr1.dtype)

int_arr = arr1.astype(int)
print(int_arr)
print(int_arr.dtype)
