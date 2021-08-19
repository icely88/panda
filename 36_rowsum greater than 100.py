import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randint(10,40,60).reshape(-1,4))
df['rowsums']=df.apply(np.sum,axis=1)
print(df)
print(df[df['rowsums']>=100].iloc[-2:]) #last two rows
