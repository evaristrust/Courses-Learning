import pandas as pd
import walter
from walter import df_frame
from purchase import total_purchase
from tools import total_tools
from service import total_service
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
print('\nTOP 10 SOLD PRODUCTS WITH HIGH REVENUES:')
print(product_name_group_desc.head(10))

#group the list of sales with their occurance count
# product_name_count_desc = product_name_group.sort_values(ascending=False)
print()
print('TOP 10 SOLD PRODUCTS WITH HIGH OCCURANCE:')
products_count = sales_action['product_sold_name'].value_counts().head(10)
print(products_count)
print()
print('ALL SOLD PRODDUCTS WITH THEIR REVENUES:')
print(product_name_group_desc)

#get the totol sold
total_sales = sales_action['total_sell_price'].sum()
print()
# print('average daily sales: {}'.format(total_sales/7))
print('\nANALYSIS OF THE STOCK VALUES FROM PUCHASE AND SALES AMOUNT')

# #create a new df containing total sales and total purchase with their difference
value_stock = total_purchase - (total_sales + total_tools + total_service)
data = [total_purchase, total_sales, total_tools, total_service, value_stock]
index = ['TOTAL PURCHASE', 'TOTAL SALES', 'TOOLS', 'SERVICES', 'VALUE IN STOCK']
columns = ['RESULTS']
df_stock = pd.DataFrame(data, index, columns)
print(df_stock.transpose())
