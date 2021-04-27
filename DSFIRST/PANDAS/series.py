import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = Series([12, 32, 21, 32])
print(obj)

#create ; index = countries, columns = money

money = [1000, 22000, 21000, 23000]
countries = ['USA', 'Germany', 'Rwanda', 'Italy']
money_obj = Series(money, index=countries)
print(money_obj)

print(money_obj['Rwanda']) # access the values using index

print(money_obj.values)

#change a series to a dict

my_dict = money_obj.to_dict()
print(my_dict)
#change dictionary back to series
my_series = Series(my_dict)
print(my_series)