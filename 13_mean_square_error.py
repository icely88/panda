import pandas as pd
import numpy as np

y=pd.Series(range(10))
y_pred=y+np.random.random(10)
#methood 1
mse= ((y-y_pred)**2).mean()
#method 2
mse=np.mean((y-y_pred)**2)
print(mse)
