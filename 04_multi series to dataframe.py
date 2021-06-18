import numpy as np
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
my_arr=[i for i in range(26)]
my_dict=dict(zip(mylist,my_arr))
ser1=pd.Series(mylist)
ser2=pd.Series(my_arr)
df=pd.DataFrame({'col1':ser1, 'col2': ser2 })
print(df)




print('only merge according to index, only merge partical data')
s1=ser1[:16]
s2=ser2[14:]
#df=pd.DataFrame({'col1':ser1, 'col2': ser2 })
df2=pd.concat([s1,s2], axis=1   )
#print(df)
print(df2)
