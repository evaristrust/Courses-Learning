import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
from pandas import Series, DataFrame

arr = np.array([[1, 2, np.nan], [3, np.nan, 4],[np.nan, np.nan, np.nan]])
frame_1 = DataFrame(arr, index=['A', 'B', 'C'], columns=['ONE', 'TWO', 'THREE'])

print(frame_1)
print(frame_1.sum()) #getting the sum of the columns automatically
print(frame_1.sum(axis=1)) #getting sum by rows
print(frame_1.min()) #getting min by columns
print(frame_1.min(axis=1)) #getting min by rows
print(frame_1.idxmin()) #getting the index with min values
print(frame_1.idxmin(axis=1)) #getting column with min values
print(frame_1.cumsum()) #getting accumulation sum
print(frame_1.cumsum(axis=1))
print(frame_1.describe()) #getting the stats

alcohol_frame = pd.read_excel(r'alcohol.xls')
#alcohol_frame.info() #there is no null value here:
print(alcohol_frame.describe())
print(alcohol_frame.plot()) #ploting the graph doesn't show right here with %matplotlib inline
