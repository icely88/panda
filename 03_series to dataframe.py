import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
my_arr=[i for i in range(26)]
my_dict=dict(zip(mylist,my_arr))
ser1=pd.Series(mylist)
ser2=pd.Series(my_arr)
print(ser1.head())
df=ser1.to_frame().reset_index()
print(df.head())
