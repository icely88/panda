import pandas as pd

airports = pd.read_csv('airports.csv')
airport_freq = pd.read_csv('airport-frequencies.csv')
runways = pd.read_csv('runways.csv')

print(airports.head())

# select * from airport_freq where airport_ident = 'KLAX' order by type
df = airport_freq[airport_freq.airport_ident == 'KLAX']
df1 = airport_freq.loc[airport_freq.airport_ident == 'KLAX']
df2 = airport_freq[airport_freq['airport_ident'] == 'KLAX']
#df1 = airport_freq[airport_freq.airport_ident == 'KLAX'].sort_values('type')
print(df.head())
print(df1.head())
print(df2.head())

# select * from airports where type in ('heliport', 'balloonport')
    df = airports[airports['type'].isin(['heliport', 'balloonport'])]
    df1 = airports.loc[airports.type.isin(['heliport', 'balloonport'])]
    print(df.head())
    print(df1.head())

# select iso_country, type, count(*) from airports group by iso_country, type order by iso_country, type
df = airports.groupby(['iso_country', 'type']).size()
print(df)

select iso_country, type, count(*) from airports group by iso_country, type order by iso_country, count(*) desc



# What is this trickery with .to_frame() and .reset_index()? 
#Because we want to sort by our calculated field (size),
# this field needs to become part of the DataFrame.
# After grouping in Pandas, we get back a different type, called a GroupByObject. 
#So we need to convert it back to a DataFrame. With .reset_index(),
# we restart row numbering for our data frame.
df=airports.groupby(['iso_country', 'type']).size().reset_index(name='count')
df=df.sort_values(['iso_country','count'], acsending=[True,False])
# select type, count(*) from airports where iso_country = 'US' group by type having count(*) > 1000 order by count(*) desc


# ['type'].value_counts()
# print(df[df >= 1000])

df = airports['type'].value_counts().reset_index(name='count')

print(df[df['count'] >= 1000])
print(df)

df = airports[airports['iso_country'] == 'US']['type'].value_counts()
print(df[df > 1000])

df = airports[airports.iso_country == 'US'].groupby('type').filter(
    lambda g: len(g) > 1000).groupby('type').size().sort_values(ascending=False)
print(df)
print(df)


# select iso_country from by_country order by size desc limit 10

df = airports[airports['iso_country'] == 'US']['type'].value_counts()
print(df.nlargest(10))


# select max(length_ft), min(length_ft), avg(length_ft), median(length_ft) from runways
print(runways.head())
print(runways['length_ft'].describe())
df = runways.agg({'length_ft': ['min', 'max', 'mean', 'median']})
print(df.T)  # transpose the data


# select airport_ident, type, description, frequency_mhz
# from airport_freq join airports on airport_freq.airport_ref = airports.id
# where airports.ident = 'KLAX'

df=airport_freq.merge(airports[airports['ident']=='KLAX'], left_on='airport_ref', right_on='id',how='inner')
df=df[['airport_ident','type','description','frequency_mhz']]


df = airport_freq.merge(airports[airports['ident'] == 'KLAX']['id'],
                        left_on='airport_ref', right_on='id', how='inner')[['airport_ident', 'type', 'description', 'frequency_mhz']]
print(df.head())


# select name, municipality from airports where ident = 'KLAX' union all select name, municipality from airports where ident = 'KLGB'
df = pd.concat([airports[airports['ident'] == 'KLAX'][['name', 'municipality']],
                airports[airports['ident'] == 'KLGB'][['name', 'municipality']]])
print(df.head())
