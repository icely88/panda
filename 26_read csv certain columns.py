
import numpy as np                     # 引入基础软件包numpy
import pandas as pd
fpath='/Users/YuanLi/Desktop/2019 job/code/testt.csv'
df=pd.read_csv(fpath, usecols=['a'])
print(df)
