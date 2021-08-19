import pandas as pd
ser = pd.Series(['01 Jan 2010',
                 '02-02-2011',
                 '20120303',
                 '2013/04/04',
                 '2014-05-05',
                 '2015-06-06T12:20'])

print(pd.to_datetime(ser))


date = pd.to_datetime(ser)
df = pd.DataFrame(data=date, columns=['dttm'])
df['week'] = df['dttm'].apply(lambda x: x.week)
df['day'] = df['dttm'].apply(lambda x: x.day)
df['month'] = df['dttm'].apply(lambda x: x.month)
df['year'] = df['dttm'].apply(lambda x: x.year)
df['hour'] = df['dttm'].apply(lambda x: x.hour)

print(df)
