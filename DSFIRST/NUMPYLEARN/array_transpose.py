import numpy as np
import pandas as pd
#1. create an array range from 6 to 100, spaced by three, 8 by 4

myarray = np.arange(6, 100, 3).reshape(8, 4)
print('MY FIRST ARRAY:')
print(myarray)
print('MY FIRST ARRAY TRANSPOSE:')
print(myarray.T)

#2. Do a dot product of two arrays
print('DOT PRODUCT ARRAY AND TRANSPOSE:')
print(np.dot(myarray, myarray.T))

print('DOT PRODUCT ARRAY TRANSPOSE AND ARRAY:')
print(np.dot(myarray.T, myarray)) #

#Try something here:
my_columns = ['A', 'B', 'C', 'D']
data = pd.DataFrame(np.arange(12).reshape(3, 4), columns=my_columns)
print('TRY SOMETHING NEW:')
print(data)
print('DELETE COLUMN B, D:')
print(data.drop(columns=['B', 'D']))
#or
print(data.drop(['B', 'D'], axis=1))

del data['A'] # this works when deleting one column~! drop is perfect
print(data)
