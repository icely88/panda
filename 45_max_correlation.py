import pandas as pd
import numpy as np
df = pd.DataFrame(
            np.random.randint(1, 100, 80).reshape(8, -1),
            columns=list('pqrstuvwxy'),
            index=list('adbcefgh')


)
abs_corrmat = np.abs(df.corr())
print(abs_corrmat)
max_corr = abs_corrmat.apply(lambda x: sorted(x)[-2])
print(max_corr)
df
