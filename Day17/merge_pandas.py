import pandas as pd

mlb_df1 = pd.DataFrame({'name': ['john doe', 'al smith', 'sam black', 'john doe'],
                        'pos': ['1B', 'C', 'P', '2B'],
                        'year': [2000, 2004, 2008, 2003]})
mlb_df2 = pd.DataFrame({'name': ['john doe', 'al smith', 'jack lee'],
                        'year': [2000, 2004, 2012],
                        'rbi': [80, 100, 12]})

print(f"{mlb_df1}\n\n")
print(f"{mlb_df2}\n\n")

merged_df = pd.merge(mlb_df1,mlb_df2,on = ['name','year']) # To understand pd.merge() refer to the documentation 
print(merged_df)



