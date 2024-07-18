import numpy as np
import pandas as pd

series = pd.Series(dtype = np.float64)
print(f"{series}\n")

series = pd.Series(5)
print(f"{series}\n")

series = pd.Series([5,6,7,8])
print(f"{series}\n")

arr = np.array([1,2,3,4])
series = pd.Series(arr,dtype = np.int16,name = "series")
print(f"{series}\n")

series = pd.Series([[1,2],[3,4],[5,6]])
print(f"{series}\n")

series = pd.Series([1,2,3,4],index = ['a','b','c','d'])
print(f"{series}\n")


# One way we can initialize pandas with the help of dictionaries in that case the key values acts as indexes for the values
series = pd.Series({'a' : 100, 'b' : 200, 'c' : 300})
print(f"{series}\n")