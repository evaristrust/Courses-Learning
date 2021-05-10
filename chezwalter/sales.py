import pandas as pd
import walter
from walter import df_frame
"""
columns: 'time_stamp', 'action', 'product_sold_name', 'quantity_sold',
         'case_sold?', 'unit_sell_price', 'total_sell_price'
"""

sales_df = df_frame[['time_stamp', 'action', 'product_sold_name', 'quantity_sold',
                            'case_sold?', 'unit_sell_price', 'total_sell_price']]

#analyse the Sales (kugurisha)
sales_action = sales_df[sales_df['action'] == 'Gucuruza'].reset_index(0)

#Change the dtype in total sales from object to int
sales_total_col = sales_action['total_sell_price']
sales_total_col = pd.to_numeric(sales_total_col)

#Group by product sold name with the total sales
product_name_group = sales_action.groupby('product_sold_name')['total_sell_price'].sum()

#group the list of sales with their amount in descending order
product_name_group_desc = product_name_group.sort_values(ascending=False)
print('TOP 10 SOLD PRODUCTS WITH HIGH REVENUES:')
print(product_name_group_desc.head(10))

#Group by product sold name with their occurance count
product_name_group = sales_action.groupby('product_sold_name')['product_sold_name'].count()

#group the list of sales with their occurance count
product_name_count_desc = product_name_group.sort_values(ascending=False)
print()
print('TOP 10 SOLD PRODUCTS WITH HIGH OCCURANCE:')
print(product_name_count_desc.head(10))
print()
print('ALL SOLD PRODDUCTS WITH THEIR REVENUES:')
print(product_name_group_desc)

#get the totol sold
total_sales = sales_action['total_sell_price'].sum()
print()
print('Total sales: {}'.format(total_sales))
print('average daily sales: {}'.format(total_sales/7))
