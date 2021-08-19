
import pandas as pd
import numpy as np

a=np.random.randint(1,10,10)
a=pd.Series(a)

print(np.argwhere(a.values % 2==0))
