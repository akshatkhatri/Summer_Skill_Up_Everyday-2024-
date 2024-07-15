import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10], dtype = np.int32)

print("arr1->",repr(arr))

## Used to Generate Values inside a range 
arr2 = np.arange(1,5,0.5)
print("arr2->",repr(arr2))

## Used to generate values from start to stop at a given number of steps
arr3 = np.linspace(1,10,10,endpoint=True)
print("arr3->",repr(arr3))

## reshapes the array into m*n or 3-d matrix or 4-d matrix as you like
arr4 = np.arange(20)

arr4_reshape = np.reshape(arr4,(4,5))
arr4_reshape2 = np.reshape(arr4,(2,-1,)) # -1 is used for unknown dimensioning 
print(repr(arr4_reshape))
print(repr(arr4_reshape2))
# print(arr4_reshape.shape)
# print(arr4_reshape2.shape)


# For Flattening an array we use .flatten 
arr5 = np.arange(8)
arr = np.reshape(arr5, (2, 4))
flattened = arr5.flatten()
print(repr(arr5))
print('arr shape: {}'.format(arr.shape))
print(repr(flattened))
print('flattened shape: {}'.format(flattened.shape))

# To transpose the Array in 2-D

arr6 = np.arange(12)
arr6 = np.reshape(arr6,(4,3))
print(repr(arr6))
arr6 = np.transpose(arr6)
print(repr(arr6))

# To Transpose the array 3-D we have to provide a axis argument (by-default-value is (2,1,0) )
arr7 = np.arange(24)
arr7 = np.reshape(arr7, (-1,4,3)) # The first index in tuple is the number of m*n matrices you have for e.g. here 2 matrices of 4*3 elements
print(repr(arr7))
print(arr7.shape)

arr7_transpose = np.transpose(arr7,axes=(1,2,0))
print(repr(arr7_transpose))
print(arr7.shape)
print(arr7_transpose.shape)


#Sometimes When dealing with Binary Data We need arrays with zeroes and ones

arr8 = np.zeros((4,5))
print(arr8)

arr8_1 = np.ones((4,5),dtype = np.int16)
print(arr8_1)

arr8_same = np.ones_like(arr7)
print(repr(arr8_same))