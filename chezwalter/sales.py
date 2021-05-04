import pandas as pd
import walter
from walter import df_frame
"""
columns:  'time_stamp', 'action', 'product_purchase_name',
'quantity_purchase', 'case_purchase?', 'unit_purchase_price', 'total_purchase_price'
"""

sales_df = df_frame.loc[:, ['time_stamp', 'action', 'product_purchase_name',
                                     'quantity_purchase', 'case_purchase?', 'unit_purchase_price',
                                     'total_purchase_price']]

#analyse the purchase (Kurangura)
sales_action = sales_df[purchase_df['action'] == 'Kurangura'].reset_index(0)
product_name_group = purchase_action.groupby('product_purchase_name')['quantity_purchase'].sum()

#Check the most purchased product
product_name_group_high = product_name_group.sort_values(ascending=False)
print(product_name_group_high.head(10))

#Check the ranges type in total_purchase_price
# 1. range 0 t0 74
column_purchase= purchase_action['total_purchase_price']
column_purchase_range1 = column_purchase[43]
print(type(column_purchase_range1))

#check if I can change the dtype in total purchase from object to int
purchase_total_col = purchase_action['total_purchase_price']
purchase_total_col = pd.to_numeric(purchase_total_col)
print(purchase_total_col.dtype)
