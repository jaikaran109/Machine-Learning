# array me basic informations frequently update krna pdta h 
# to bahut se inbuilt functions hai jpo help krte h 
# ye original array me changes nhi krta h ye copy create krta h 


'''  INSERTION
array - original array
index -
value -
axis = 0,row-wise insertion -- by default its 0
1 column wise insertion 

agr axis = none krte h to vo flatten version me insert kr dega 
        arr=    [[1,2]
                [3,4]]
    new arr    [1 5 6 2 3 4]
'''

import numpy as np

# 1D Array

arr_1d =  np.array([10,20,30,40,50,60])
new_arr_1d = np.insert(arr_1d,2, 100)
print(arr_1d)
print("insertion in 1D array",new_arr_1d)




# 2D ARRAY

arr_2d = np.array([[1,2],[3,4]])
print(arr_2d)
new_arr_2d = np.insert(arr_2d,1,[5,6],axis=0) # insert a new row at index 1
print("\n insertion in 1D array",new_arr_2d)




# Append --- jb last me elements add krne ho to
arr = np.array([10,20,30])
new_arr = np.append(arr,[40,50,60])
print("\n append array ",new_arr) 




# Concatinate array
'''
np.concatenate(array1,array2,axis = 0)

axis 0 > vertical stacking
axis 1 > horizontal stacking
'''

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
new_arr3 = np.concatenate((arr1,arr2))
print("\n concatenate array",new_arr3)





#removing elements from array -- np.delete(array,index,axis = none) -- none means dlt from flatten array (means 1d array)
# -- 1D array
original_arr1D = np.array([10,20,30,40,50,60])
print("\n original 1D array",original_arr1D)
removed_arr1D = np.delete(original_arr1D,0)
print("1D array after removing",removed_arr1D)

# -- 2D array
original_arr2D = np.array([[10,20,30],[40,50,60]])
print("\n original 2D array",original_arr2D)
removed_arr2D = np.delete(original_arr2D,0,axis=0)
print("2D array after removing",removed_arr2D)
