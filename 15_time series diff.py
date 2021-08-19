import pandas as pd
import numpy as np
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])

print('first level of diff', ser.diff())
print('second levle of diff', ser.diff().diff()  )
