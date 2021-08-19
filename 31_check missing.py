import pandas as pd
import numpy as np
df = pd.DataFrame({
   'a':[1.2,2,3,4],
    'b':list('abcd')
})

print(df)
print(df.isnull().values.any())
df.iat[0,0]=np.nan
print(df)
print(df.isnull().values.any())

print(df.apply(lambda x:x.isnull().sum() ))
