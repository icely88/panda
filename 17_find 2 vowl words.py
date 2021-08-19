import pandas as pd
import numpy as n

ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
def count(x):
    s='aouie'
    c=0
    for i in x:
        if i in s:
            c+=1
    return c

counts=ser.map(lambda x: count(x))
print(ser[counts>=2])
print(ser)


df=pd.DataFrame(ser,columns=['fruit'])
df['count']=df['fruit'].apply(lambda x: count(x))
print(df[df['count']>1])

print(df[d])
