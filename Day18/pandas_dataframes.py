import pandas as pd

data = pd.DataFrame([[1,2],[3,4]],
                    index = ['r1','r2'],
                    columns = ['c1','c2'])
print(data)

# one more way to do initialization is to follow the same dictionary method in this keys serve as column indexes

data = pd.DataFrame({'c1' : [1,2], 'c2' : [3,4]},
                    index = ['r1', 'r2'])
print(data)

# Type-casting happens on column basis rows remain unaffected

data = pd.DataFrame([[1,2.6],[3,4]],
                    index = ['i','ii'],
                    columns = ['A','B'])
print(data)
print(data.dtypes) # as can be seen in this output only the columns were typecasted




