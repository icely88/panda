import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randint(1, 30, 30).reshape(10,-1),
    columns=list('abc'))
print(df['a'])
print(df['a'].argsort())
print(df['a'].argsort().iloc[9]) # sort by row number, the row number of max value
