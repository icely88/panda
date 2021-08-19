import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.random(4)**10, columns=['random'])
print(df.head())

pd.set_option('display.float_format', lambda x: '%.4f' %x)
df=pd.DataFrame(np.random.random(4)**10, columns=['random'])
print(df.head())
