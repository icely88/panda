import pandas as pd
import numpy as np

time=pd.Series (np.random.randint(1,10,10),
           pd.date_range('2000-01-02',periods=10, freq='W-SAT')


)
print(time  )
