import pandas as pd
import numpy as np
ser=pd.Series(np.random.randint(1,10,35))
df=pd.DataFrame(ser.values.reshape(7,5))

print(df)
