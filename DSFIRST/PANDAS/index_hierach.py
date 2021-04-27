import numpy as np
import pandas as pd
from numpy.random import randn
from pandas import Series, DataFrame

#we are going to learn indexing hierachy

my_series = Series(randn(6), index=[[1,1,1,2,2,2], ['a','b','c','a','b','c']])
print(my_series)
print(my_series.index)
print(my_series[1]) #accessing index data
print(my_series[1]['a'])
print(my_series[:, 'a'])

#creating a df from multilevel index series using unstack

df = my_series.unstack()
print(df)

df2 = DataFrame(np.arange(24).reshape(4,6), index=[['a','a','b','b'], [1,2,1,2]],
                columns=[['MUTZIG', 'MUTZIG','SKOL', 'SKOL', 'AMSTEL', 'AMSTEL'],
                         ['Hot','Cold', 'Hot', 'Cold', 'Hot', 'Cold']])
print(df2)

# you can also namer indices or columns
df2.index.names = ['INDEX_1', 'INDEX_2']
df2.columns.names = ['BEERS', 'TEMPERATURE']
print(df2)

#you can also swaplevels
df2_swap = df2.swaplevel('BEERS', 'TEMPERATURE', axis=1)
print(df2_swap)

#let's do sum for cold and hot
df2_sum = df2.sum(level='TEMPERATURE', axis=1)
print(df2_sum)