import pandas as pd
import numpy as np
import csv
fpath='/Users/YuanLi/Desktop/2019 job/code/testt.csv'
df=pd.DataFrame(
               {'a': range(100),
               'b':np.random.choice(['apple','banana','carrot'],100)

               }
)
#print(df.head(19))
df.to_csv(fpath,index=None)

with open(fpath,'r') as f:
    reader=csv.reader(f)
    out=[]
    for i, row in enumerate(reader):
        if i%20==0:
            out.append(row)
print(pd.DataFrame(out[1:], columns=out[0]))
