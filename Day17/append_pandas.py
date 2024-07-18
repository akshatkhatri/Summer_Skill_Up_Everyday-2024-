import pandas as pd

df = pd.DataFrame([[1,2,3],[3.5,4,5]])
ser = pd.Series([6,7,8],index = df.columns,name = "r3")

# we will be using df.concat as df.append is depreceated

df_app = pd.concat([df,ser.to_frame(ser.name).T],ignore_index = True)
print(df_app)

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index = ['i','ii','iii'],columns = ['A','B','C'])
df2 = pd.DataFrame([[11,22,33],[44,55,66],[77,88,99]],index = ['i','ii','iii'],columns = ['A','B','C'])

df_app = pd.concat([df,df2],ignore_index = True)
print(df_app) # This concatenation is done along rows

df_app = pd.concat([df,df2],ignore_index = True,axis = 1)
print(df_app)

# WE can also drop these tables by using df.drop() and if we set inplace = true , in-place dropping is done

df2.drop(index = ['i'],columns = ['A'], inplace = True)
print(df2)

