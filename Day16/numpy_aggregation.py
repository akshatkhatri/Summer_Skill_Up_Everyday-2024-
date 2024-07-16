import numpy as np

# We know how to sum multiple arrays but when adding the elements of arrays we use np.sum() method

arr = np.array([[0, 72, 3],
                [1, 3, -60],
                [-3, -2, 4]])

print(np.sum(arr))
print(np.sum(arr,axis = 0))
print(np.sum(arr, axis = 1))

# If we want to have the cumulative sum of the numbers at each index we can use np.cumsum() 
# Note that cumsum() returns cumultavie frequencies at each index while sum() returns just the sum
# np.cumsum() output has same size as the input matrix

print(repr(np.cumsum(arr)))
print(repr(np.cumsum(arr,axis = 0))) # cumulative sum across the columns
print(repr(np.cumsum(arr, axis = 1))) # cumulative sum across the rows

# We also have np.concatenate() function which concatenates the two matrices or arrays 
# if no axis is specified it flattens and then joins them if axis is specified it does so along the axis
# please note that concatenation doesn't mean adding up it just simply puts b at the end of a

arr1 = np.array([[0, 72, 3],
                 [1, 3, -60],
                 [-3, -2, 4]])
arr2 = np.array([[-15, 6, 1],
                 [8, 9, -4],
                 [5, -21, 18]])

print(repr(np.concatenate([arr1,arr2])))
print(repr(np.concatenate([arr1,arr2],axis = 0)))
print(repr(np.concatenate([arr1,arr2],axis = 1)))
print(repr(np.concatenate([arr2,arr1],axis = 1)))

