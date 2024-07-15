import numpy as np

rand_num = np.random.randint(100)
print(rand_num)
arr = np.random.randint(low = -3,high = 0,size = (3,3))
print(repr(arr))
''' # The code below is commented out as to not affect the output of the other program
# The seed function in the np.random.seed() , seeds the value for the random number generation

# np.random.seed(1) 
# print(np.random.randint(10)) # the output will be the same value again and again due to same seed

# print(np.random.randint(low = 1 , high =10, size =(3,3))) #  the output will be the same value again and again due to same seed

# the shuffle function shuffles the values in-place along the first dimension only
'''
vec = np.array([1,2,3,4,5,6])
np.random.shuffle(vec)
print(repr(vec))

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

np.random.shuffle(matrix)
print(repr(matrix)) # Note that shuffling will only take place in the first dimension i.e. Rows-only 


# The below code is for continous distribution function producing decimal values
arr = np.random.uniform(low = -3, high = 0, size=(3,3))
print(repr(arr))

# and for generating a normal distribution with bell-shaped curve , in this case the more we move far away from mean less likely to get that value

arr = np.random.normal(loc = 1.5,scale = 3.5,size = 5)
print(repr(arr))

# we Can also randomize our own list 

colors = ["Red","Green","Blue","Yellow","Purple"]
print(np.random.choice(colors))
print(np.random.choice(colors,size = (3,3)))
print(np.random.choice(colors,size = (3,3),p=[0.1,0.6,0.1,0.1,0.1])) # The p argument is used for specifying the probabilties of the array

arr = np.array()