import pandas as pd

'''Index(['customer_name', 'district_name', 'sector_name', 'signed_by',
       'product_interest', 'currency', 'floor_size', 'contract_type',
       'amount'],'''

df = pd.read_excel(r'D:\PERSONALS\EE\SALESFORCE REPORTS\SALES\rwandasales.xlsx')

#1. chech the shape of our dataset
# table_shape = df.shape
#
# print('The shape of our data is:', table_shape)

#2. change the columns naming
new_names = ['customer_name', 'district_name', 'sector_name', 'signed_by',
             'product_interest', 'currency', 'floor_size', 'contract_type', 'amount']

df.set_axis(new_names, axis='columns', inplace=True) # in place True means the original data set will be modified
#
# print(df.shape)
# print(df.columns)

#3. checking the missing values and set them to unknown or zero
# print('isna values:', df.isna().sum()) # found 1 in floor_size (set=0) & 3 in contract_type(set=unknown)
df['contract_type'] = df['contract_type'].fillna('unknown')
df['floor_size'] = df['floor_size'].fillna(0)

#check the main info of our dataset
# df.info()

#4. Going to study columns : customer_name, district_name, floor_size, signed_by, product_interest and amount

my_first_table = df.loc[:, ['district_name', 'customer_name', 'signed_by', 'product_interest', 'floor_size', 'amount']]
top_10 = my_first_table.head(10) #printing the top 10 rows of our data

#5. check how many missing cells in each column! Not necessary

# print('Missing values in District_name: ', my_first_table['district_name'].isnull().sum())
# print('Missing values in product_interest: ', my_first_table['district_name'].isnull().sum())
# print('Missing values in floor_size: ', my_first_table['district_name'].isnull().sum())
# print('Missing values in amount: ', my_first_table['district_name'].isnull().sum())

#6. check the duplicates values accross the table

#print('number of duplicates:', df.duplicated().sum()) #yaay! There are no duplicates rows!

# 7. Analyse the total number of contracts in each district

group_districts_count = my_first_table.groupby('district_name')['product_interest'].count()
print('\nNumber of contracts sold in each district this year')
print(group_districts_count)

#8. total sqm per district
print('\n****Total sqm per district******')

group_districts_sqm = my_first_table.groupby('district_name')['floor_size'].sum()
print('Total districts:', group_districts_sqm.shape[0])
print(group_districts_sqm)

#9. sort to see the top 5 performing districts in sales

sort_count = group_districts_count.sort_values(ascending=False)
sort_sum = group_districts_sqm.sort_values(ascending=False)
final_count = sort_count.head(5)
final_sum = sort_sum.head(5)

print('\nTOP 5 PERFORMING DISTRICTS 2021--SALES COUNTS')
print('TOTAL DISTRICTS IN EE RWANDA:', group_districts_sqm.shape[0])
print(final_count)

print('\nTOP 5 PERFORMING DISTRICTS 2021--TOTAL SQMS SOLD')
print('TOTAL DISTRICTS IN EE RWANDA:', group_districts_sqm.shape[0])
print(final_sum)

#9. sort to see the top 5 under-performing districts in sales

sort_count_under = group_districts_count.sort_values(ascending=True)
sort_sum_under = group_districts_sqm.sort_values(ascending=True)
final_count_under = sort_count_under.head(5)
final_sum_under = sort_sum_under.head(5)

print('\nTOP 5 UNDER-PERFORMING DISTRICTS 2021--SALES COUNTS')
print('TOTAL DISTRICTS IN EE RWANDA:', group_districts_sqm.shape[0])
print(final_count_under)

print('\nTOP 5 UNDER-PERFORMING DISTRICTS 2021--TOTAL SQMS SOLD')
print('TOTAL DISTRICTS IN EE RWANDA:', group_districts_sqm.shape[0])
print(final_sum_under)

#10. sorting the top districts in Revenues
group_districts_amount= my_first_table.groupby('district_name')['amount'].sum()
print('Total districts:', group_districts_sqm.shape[0])

sort_sum_amount = group_districts_amount.sort_values(ascending=False) # sorting desc order
final_sum_amount = sort_sum_amount.head(5)

print('\nTOP 5 PERFORMING DISTRICTS 2021--TOTAL SALES REVENUES')
print('TOTAL DISTRICTS IN EE RWANDA:', group_districts_amount.shape[0])
print(final_sum_amount)


sort_sum_amount_under = group_districts_amount.sort_values(ascending=True) # sorting desc order
final_sum_amount_under = sort_sum_amount_under.head(5)

print('\nTOP 5 UNDER-PERFORMING DISTRICTS 2021--TOTAL SALES REVENUES')
print('TOTAL DISTRICTS IN EE RWANDA:', group_districts_amount.shape[0])
print(final_sum_amount_under)

#11. check the maximum house countrywide
check_max = my_first_table['floor_size'].max()
print('\nmaximum size floor size countrywide:', check_max)
check_max_info = my_first_table[my_first_table['floor_size'] == check_max]
print(check_max_info.loc[:, ['district_name', 'product_interest', 'floor_size', 'signed_by']])

#12. check the minimum house countrywide
check_min = my_first_table['floor_size'].min()
print('\nminimum size floor size countrywide:', check_min)
check_min_info = my_first_table[my_first_table['floor_size'] == check_min]
print(check_min_info.loc[:, ['district_name', 'floor_size', 'customer_name']])

#13. check the maximun revenue countryside per floor and their details
check_max_amount = my_first_table['amount'].max()
print('\nmaximum Revenue per floor countrywide:', check_max_amount)
check_max_amount_info = my_first_table[my_first_table['amount'] == check_max_amount]
print(check_max_amount_info.loc[:, ['district_name', 'floor_size', 'customer_name']])

#14. check the minimum revenue countryise per floor and its details
min_zero_filter = my_first_table[my_first_table['amount'] > 0]
check_min_amount = min_zero_filter['amount'].min()
print('\nminimum Revenue per floor countrywide:', check_min_amount)
check_min_amount_info = my_first_table[my_first_table['amount'] == check_min_amount]
print(check_min_amount_info.loc[:, ['district_name', 'floor_size', 'customer_name']])

#15. group by product interests and sort the sum of their amounts in descending order
print('\nRevenues per product interests:')
product_interest_group = my_first_table.groupby('product_interest')['amount'].sum().sort_values(ascending=False)
print(product_interest_group)

#16. maximum house in each district and sort them desc order
print('\nMaximum floors by district; sorted in descending order:')
check_max_group = my_first_table.groupby('district_name')['floor_size'].max().sort_values(ascending=False)
print(check_max_group)
