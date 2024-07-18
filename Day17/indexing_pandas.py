import pandas as pd

df = pd.DataFrame({'c1': [1, 2], 'c2': [3, 4],
                   'c3': [5, 6]}, index=['r1', 'r2'])

val1 = df['c1'] # when using a single value inside the series we get a series object
print(val1)

val2 = df[['c1','c2']] # when using two or more arguments inside square brackets we get a DATA FRAME
print(val2)

# We can use iloc for indexing with integers 

df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])
print(f"{df}\n")
print(df.iloc[2])
print(df.iloc[0 : 2])


# loc works the same way as iloc , the only catch being that it uses row labels for indexing

df = pd.DataFrame({'c1': [1, 2, 3], 'c2': [4, 5, 6],
                   'c3': [7, 8, 9]}, index=['r1', 'r2', 'r3'])

print(df.loc['r3'])
print(df.loc['r2','c2'])

print(df.loc[['r1','r3'],'c2'])