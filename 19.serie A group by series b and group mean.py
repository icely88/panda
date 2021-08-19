import pandas as pd
import numpy as np

fruit=pd.Series(np.random.choice(['apple','banana','carrot'], 10))
weight=pd.Series(np.linspace(1,10,10))
print(fruit)
print(weight)


print(weight.groupby(fruit).sum())

df=pd.DataFrame( {
                'fruit':fruit,
                'weight': weight
                 }
                 )

print(df.groupby(fruit).sum())
print(df.groupby(fruit).mean())
print(df.groupby(fruit).max())
