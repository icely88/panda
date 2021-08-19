import pandas as pd
import numpy as np

ser=pd.Series(np.arange(20)+np.random.normal(1,10,20))
print(ser)

autocorrelation=[ser.autocorr(i).round(2) for i in range(11)]
print(autocorrelation)
