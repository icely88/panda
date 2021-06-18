import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
my_arr=[i for i in range(26)]
my_dict=dict(zip(mylist,my_arr))
ser1=pd.Series(mylist)
print(ser1.head())
