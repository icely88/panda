import pandas as pd
import numpy as np

ser = pd.Series(['how', 'to', 'kick', 'ass?'])

#captilize first letter
ser=ser.map(lambda x:x.title())
#capitalize all letter
ser=ser.map(lambda x:x.upper())
print(ser)

#length of each elements
ser2=ser.map(lambda x:a len(x))
print(ser2)
