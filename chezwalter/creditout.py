import pandas as pd
import walter
from walter import df_frame
"""
columns:  'time_stamp', 'action', 'product_credited', 'product_cred_quantity', 'product_cred_case?',
'product_cred_unit_price', 'product_cred_total', 'debtor_name'
"""
#Study of credits given out
#Notify based on the maximum credit set

credit_df = df_frame.loc[:, ['time_stamp', 'action', 'product_credited', 'product_cred_quantity',
                               'product_cred_case?', 'product_cred_unit_price', 'product_cred_total',
                               'debtor_name']]

#analyse the purchase (Kurangura)
cred_action = credit_df[credit_df['action'] == 'Ideni'].reset_index(0)

#check if I can change the dtype in total purchase from object to int
cred_total_col = cred_action['product_cred_total']
cred_total_col = pd.to_numeric(cred_total_col)

#Get the total business credit on products
total_credits = cred_total_col.sum()
print('THE TOTAL BUSINESS CREDITS:{}RWF'.format(total_credits))
