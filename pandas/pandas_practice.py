# https://www.kaggle.com/learn/pandas
import pandas as pd 

df = pd.DataFrame({"YES":[50,21],"No":[131,2]})

print(df)

df_with_index = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print(df_with_index)

se = pd.Series([30,45,40], index=["Sales 2015","Sales 2016","Sales 2017"], name='Prodcut A')
print(se)


######
df_wine = pd.read_csv('winemag-data-130k-v2.csv')
print(df_wine.shape)

print(df_wine.head())
df_wine = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
print(df_wine.head())
#####Indexing, selecting & Assigning 
print(df_wine.country)
print(df_wine['country'][0])
print(df_wine.iloc[0]) #get 0th row

print(df_wine.iloc[:,0]) # get retrieve 0th  columns and all the rows
print(df_wine.iloc[:3,0]) #retrieve 3 rows of 0th column 
print(df_wine.iloc[[0,1,2], 0]) #result same as above
print(df_wine.iloc[-5:]) # last five elements 

print(df_wine.loc[0, 'country'])  #Italy 
print(df_wine.loc[:3, ['taster_name', 'taster_twitter_handle', 'points']])
df_wine= df_wine.set_index('title')
print(df_wine.head())
print(df_wine.loc[(df_wine.country == 'Italy') | (df_wine.points >= 90)])

print(df_wine.loc[df_wine.country.isin(['Italy', 'France'])])
print(df_wine.loc[df_wine.price.notnull()])

# df_wine['critics'] = 'everyone'
# print(df_wine)
df_wine['index_backwards'] = range(len(df_wine),0, -1)
print(df_wine)


# Summary Functions and Maps
print(df_wine.points.describe())  #for int type column
print(df_wine.taster_name.describe())  #for str type column , syntax is same for both int and str but o/p is differ

#mean()
print(df_wine.points.mean())
#unique
print(df_wine.taster_name.unique())

# To see a list of unique values and how often they occur in the dataset, we can use the value_counts() method:
print(df_wine.taster_name.value_counts())

#map()
review_points_means = df_wine.points.mean()
# print(df_wine.points.map(lambda p: p - review_points_means))

#apply()
# def remean_points(row):
#     row.points = row.points - review_points_means
#     return row

# df_wine = df_wine.apply(remean_points, axis='columns')
# print(df_wine.loc[:,['country','points']])

######Grouping and sorting 
# print(df_wine.points.value_counts())
# print(df_wine.groupby('points').points.count())
# print(df_wine.groupby('points').price.min())
# print(df_wine['title'].head(5))
# print(df_wine.columns)
# print(df_wine.groupby('winery').apply(lambda df: df.title.iloc[0]))

print(df_wine.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()]))

print(df_wine.groupby(['country']).price.agg([len,max,min]))

countries_reviewed = df_wine.groupby(['country','province']).description.agg([len])
# print(countries_reviewed)
mi = countries_reviewed.index
# print(type(mi))
countries_reviewed.reset_index(inplace=True)
# print(countries_reviewed)

#sort by
print(countries_reviewed.sort_values(by='len')) #ascending
print(countries_reviewed.sort_values(by='len', ascending=False)) #descending
print(countries_reviewed.sort_index())

# print(countries_reviewed.sort_values(by=['country', 'len']))

# Data Types and Missing Values
# print(df_wine.dtypes)
# df_wine1 = df_wine.points.astype('float64')  #to convert column to another dtype
# print(df_wine1.dtypes)

print(df_wine.index.dtype)
###missing data 
print(df_wine[pd.isna(df_wine.country)])
#fillna, replace 
df_wine.region_2.fillna('Unknown')
df_wine.taster_twitter_handle.replace("@kerinokeefe", "@kerino")


# Renaming and Combining
print(df_wine.columns)
tt = df_wine.rename(columns={'points':'score'})
# print(tt.columns)
# index renaming, but this we can use rarely. 
tt = df_wine.rename(index={0: 'firstEntry', 1:'secondEntry'})
print(tt.head(5))
#we can use like below for setting index 
tt=df_wine.rename_axis("wines", axis='rows').rename_axis('fields', axis='columns')
print(tt)
