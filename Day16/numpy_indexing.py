import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(repr(arr[:]))
print(repr(arr[1:]))
print(repr(arr[2:4]))
print(repr(arr[:-1]))
print(repr(arr[-2:]))

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(repr(arr[:]))
print(repr(arr[:-1]))
print(repr(arr[0:1,1:])) #First selects the first row and then slices from col 1 to end
print(repr(arr[0,0:])) # When slicing a 2-D matrix we can use comma to specify index in that single dimension

# We can use argmin and argmax for finding min max elements , argmin & argmax returns the indices and if whole array is provided as arguments returns the flattened array version

arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])

print(repr(np.argmin(arr[0])))
print(repr(np.argmax(arr[1])))

print(repr(np.argmin(arr))) # returns 5 as index in flattened array
print(repr(np.argmax(arr))) # returns 7 for flattended array 



# One more argument can be provided into argmin and argmax namely axis = 0(row element for each column) , 1(column element for each row) , -1(last axis)

arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [-3, 9, 1]])

print(repr(np.argmin(arr, axis=0)))  # Find the index of the minimum value along columns
print(repr(np.argmin(arr, axis=1)))  # Find the index of the minimum value along rows
print(repr(np.argmax(arr, axis=-1)))  # Find the index of the maximum value along the last axis (rows in this case)
