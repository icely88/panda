import pandas as pd
import numpy as np
d={"col1":[1,2,3],"col2":["A","B","C"]}
df=pd.DataFrame(d)



df1 =df.drop(["col1"],axis=1)
print(df1)

df2=df[df.col1!=1]
print(df2)
