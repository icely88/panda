import pandas as pd
import numpy as np

df=pd.DataFrame(np.arange(20).reshape(-1,5), columns=list('abcde'))
print(df.head())

print(df[list('cbade')])
