import pandas as pd
import numpy as np

ser=pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01','2000-01-03','2000-01-06','2000-01-08']))
print(ser.resample('D').ffill())
