'''
np.split()
equal

np.hsplit()
np.vsplit()

(arr,no. of parts)  -- if number of split is more than number of element then it's generate error
'''

import numpy as np
arr = np.array([10,20,30,40,50,60])
print(np.split(arr,2))
