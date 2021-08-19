import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1))
print(df)
nearest = {}
for i, row in df.iterrows():
    c = ((df-row)**2).sum(axis=1).argsort()
    print(c)  # rank by smallest distance index, the top always itself
    for j in c:
        if j != i:
            break
    nearest[i] = j
print(nearest)
#for i, row in df.
print(df)
