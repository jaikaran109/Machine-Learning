#reshaping -- change dimensions without modifying data
#1d array - 2d
#2d - 3d


#arr.reshape()
#total numbers are same 
# EX -- [1,2,3,4]  changed -- [[1,2],[3,4]]



#RESHAPE 
'''
reshape(wors,columns) specify new shape
if dimensions match

-- reshape does not creat copy it creat a view
'''
import numpy as np
arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)




