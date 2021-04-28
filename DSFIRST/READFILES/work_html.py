import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandas import read_html

url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list'

df_list = pd.io.html.read_html(url)
df = df_list[0]
print(df.columns)