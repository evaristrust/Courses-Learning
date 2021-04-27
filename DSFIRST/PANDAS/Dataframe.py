import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data = pd.read_clipboard()
print(data)
print(data.columns)
new_names = ['date', 'expenses', 'amount', 'iou', 'receipt', 'paid']
new_data = data.set_axis(new_names, axis='columns')
print(new_data)
print(new_data['expenses'])

analysis = new_data.loc[:, ['date', 'expenses', 'amount']]
print(analysis)

# construct a DataFrame from a dictionary
cities = {'City_name': ['KGL', 'NG', 'KY'], 'employees': [20, 21, 11]}
cities_frame = DataFrame(cities)
print(cities_frame) #series or datafrome is created from dictionaries

print(new_data.describe())