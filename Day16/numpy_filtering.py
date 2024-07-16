import numpy as np

# WE can use comparisons the same way we do it with simple numbers 
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,np.nan]])

print(repr(arr == 3))
print(repr(arr > 0))
print(repr(~(arr <= 5)))
print(np.isnan(arr))

# The np.where() function when taking 1 argument
# RETURNS AN array with elements from x where condition is True, and elements from y elsewhere.

print(repr(np.where([True,False,True,False,False,True])))

arr = np.array([0, 3, 5, 3, 1])
print(repr(np.where(arr == 3))) # arr = 3 will return a boolean array and np.where() returns the true indices

arr = np.array([[0, 2, 3],
                [1, 0, 0],
                [-3, 0, 0]])
x_ind , y_ind = np.where(arr < 3)
print(repr(x_ind)) # returns the x-indices of the places where arr < 3 for e.g. first value in output is 0
print(repr(y_ind)) # Returns the corresponding y-axis of the places where arr < 3, second value in output is 0 as arr[0[0]] < 3

print(repr(arr[x_ind, y_ind]))


# When np.where takes 3 arguments first the boolean array , second and third are the values we want to replace true and false with respectvely
arr = np.array([[0, 2, 3],
                [1, 0, 0],
                [-3, 0, 0]])

print(repr(np.where(arr == 3, 3, np.nan)))

# WE can also provide arrays as arguments in where()
arr = np.array([[0, 2, 3],
                [-1, 0, 0],
                [-3, 0, 0]])

positives = [ [1,1,1],
             [2,2,2],
             [3,3,3] ]
negatives = [ [-1,-1,-1],
             [-2,-2,-2],
             [-3,-3,-3] ]

print(repr(np.where(arr >= 0, positives,negatives))) # The greater than 0 values will be replaced by the corresponding x-value and the less than 0 will be replaced by corresponding y-value


# np.any() and np.all() when provided with a single argument ,does a logical OR(||) and logical AND(&&) respectively
# When called with a single argument it returns a single boolean

arr = np.array([[-2, -1, -3],
                [4, 5, -6],
                [3, 9, 1]])

print(repr(arr > 0))
print(repr(np.any(arr > 0)))
print(repr(np.all(arr > 0)))

# However if we use multi-dimensional



