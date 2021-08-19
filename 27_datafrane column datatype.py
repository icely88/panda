import numpy as np                     # 引入基础软件包numpy
import pandas as pd

df=pd.DataFrame(
            {
                'a':range(100) ,
                'b':np.random.rand(100),
                'c':[1,2,3,4]*25,
                'd':['apple','banana','carrot']*33+['apple']


            }




)

print(df.dtypes)  #data dtypes#
print(df.shape)  #data dimension
print(df.describe())

print(df.loc[df.a==np.max(df.a)])  #method1: find column a max , return its row
print(df[df['a']==df['a'].max()])  #method2: find column a max , return its row


print(df[df['c']==df['c'].max()].index)  #row number of c column max value
print(np.where(df.c==np.max(df.c)))
