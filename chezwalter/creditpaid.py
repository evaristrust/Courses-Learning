import pandas as pd
import walter
from walter import df_frame
from creditout import total_credits
"""
columns:  'time_stamp', 'action', 'debtor_name', 'credit_balance', 'total_repay'
"""
#Study of credits given out
#Notify based on the maximum credit set


cred_paid_df = df_frame.loc[:, [ 'time_stamp', 'action', 'debtor_name', 'credit_balance', 'total_repay']]

#analyse the purchase (Kurangura)
cred_paid_action = cred_paid_df[cred_paid_df['action'] == 'Kwishyura ideni'].reset_index(0)

#check if I can change the dtype in total purchase from object to int
repaid_col = cred_paid_action['total_repay']
repaid_col = pd.to_numeric(repaid_col)

#Get the total business credit on products
total_credits_repaid = repaid_col.sum()

#create a function to allow more credit or not
def allow_cred():
    max_credit = 10000
    unpaid_credit = total_credits - total_credits_repaid # difference btn credits and repaid credit (balance)
    absolute_extra = abs(max_credit - unpaid_credit)
    if unpaid_credit < 10000:
        print('You are allowed to give credits of no more than {}RWF'.format(absolute_extra))
    else:
        print('No, you can\'t give credits... Reached maximum with extra amount of {}RWF'.format(absolute_extra))
    print('Your unpaid credit is {}RWF'.format(unpaid_credit))

allow_cred()
