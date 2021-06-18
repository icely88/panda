import pandas as pd
import numpy as np
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

print ('ser1 not in ser2')
print(ser1[~ser1.isin(ser2)])


print('--------------------')
print('unique elements in two series')
print(np.union1d(ser1,ser2))

print('common elements in two series')
print(np.intersect1d(ser1, ser2))

print('--------------------')
print('uncommon elements in two series')

u=pd.Series(np.union1d(ser1,ser2))
i=pd.Series(np.intersect1d(ser1, ser2))
print(u[~u.isin(i)])
