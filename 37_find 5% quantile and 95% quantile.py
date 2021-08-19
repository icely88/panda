import pandas as pd
import numpy as np

ser=pd.Series(np.logspace(-2,2,30))  #10^-2 to 10^2  30 numbers
print(ser)
print(10**(-2))

low,high=ser.quantile([0.05, 0.95])
print(low,high)

ser[ser<low]=low
ser[ser>high]=high

df=pd.DataFrame(ser,columns=['a'])
df[df['a']<low]=low
print(df)
