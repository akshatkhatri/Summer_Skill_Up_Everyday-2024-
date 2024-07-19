import pandas as pd

df = pd.DataFrame({
  'T1': [10, 15, 8],
  'T2': [25, 27, 25],
  'T3': [16, 15, 10]})

print(f"{df}\n")
print(f"{df.sum()}\n")
print(f"{df.sum(axis = 1)}\n")

print(f"{df.mean()}\n")
print(f"{df.mean(axis = 1)}\n")

