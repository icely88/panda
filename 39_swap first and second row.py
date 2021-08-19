import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(25).reshape(5,-1))
print(df)
a,b=df.iloc[1,:].copy(), df.iloc[2,:].copy() # will make sure the original datafram not change; without copy, the df will not remember the change
print('a:', a)
print('b',b)

df.iloc[1,:]=b
df.iloc[2,:]=a
print(df)


print(df.iloc[::-1,:]) # output from last row

pd.get_dummies(df['a'])
