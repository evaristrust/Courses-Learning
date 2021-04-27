import numpy as np
import pandas as pd
from pandas import Series, DataFrame

arr = np.array([[1, 2, np.nan], [3, 8, np.nan],[np.nan, np.nan, np.nan]])
frame_1 = DataFrame(arr, index=['A', 'B', 'C'], columns=['ONE', 'TWO', 'THREE'])

print(frame_1)

#drop the nan ... will delete every row with nan value
dropped_nan = frame_1.dropna() #specify axis when dropping columns
print(dropped_nan) # will remain with one .. highly not recommended
dropped_empty_row = frame_1.dropna(how='all')
print(dropped_empty_row) #this is clean enough
dropped_empty_col = frame_1.dropna(axis=1, how='all')
print(dropped_empty_col)