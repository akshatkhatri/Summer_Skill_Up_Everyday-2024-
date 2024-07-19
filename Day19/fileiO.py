import pandas as pd

df = pd.read_csv("data.csv",index_col = 0)

print(f"{df}\n\n") 

# HOW to read JSON 

df1 = pd.read_json("sample.json")
print(f"{df1}\n")


df1 = pd.read_json("sample.json",orient = "records")
print(f"{df1}\n")

# Functions on writing to a CSV file

mlb_df1 = pd.DataFrame({'name': ['john doe', 'al smith', 'sam black', 'john doe'],
                        'pos': ['1B', 'C', 'P', '2B'],
                        'year': [2000, 2004, 2008, 2003]})

mlb_df1.to_csv("employee.csv",index = False)

mlbr_df1 = pd.read_csv("employee.csv")
print(f"{mlbr_df1}\n")


# FUnctions on writing to a json file

# Predefined df
print('{}\n'.format(df))

df.to_json('data.json')
df2 = pd.read_json('data.json')
print('{}\n'.format(df2))

df.to_json('data.json', orient='index')
df2 = pd.read_json('data.json')
print('{}\n'.format(df2))
df2 = pd.read_json('data.json', orient='index')
print('{}\n'.format(df2))