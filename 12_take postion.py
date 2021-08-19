import pandas as pd
import numpy as np

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos=[0,3,4,5]
print(ser.take(pos))

aims=list('adhz')
a=[pd.Index(ser).get_loc(i) for i in aims]
print(a)

print(pd.Index(ser).get_loc('s'))

#https://www.geeksforgeeks.org/python-pandas-series-loc/
