import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# df['Min.Price'].apply(lambda x: x.fillna(x.mean()))
print(df['Min.Price'].head())

df=df[['Min.Price']].apply(lambda x: x.fillna(x.mean())).head()  #please note the double []
print(df.head())
