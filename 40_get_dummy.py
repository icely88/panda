import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(25).reshape(5,-1), columns=['a','b','c','d','e'])
print(df)

dummy_a=pd.get_dummies(df['a'])
df=pd.concat([dummy_a, df[list('bcde')]],axis=1)
print(df)
