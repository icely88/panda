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

df=df.rename(columns={'d':'fruit'})
print(df.head())
