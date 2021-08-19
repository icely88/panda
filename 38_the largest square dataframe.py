import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
print(df)

arr=df[df>0].values.flatten()
print(arr)
arr_qualified=arr[~np.isnan(arr)] #not null array
print(arr_qualified)
n=int(np.floor(arr_qualified.shape[0]**0.5)) # note floor and int difference
print(n)
output=arr_qualified[:n**2].reshape(n,-1)
print(output)
