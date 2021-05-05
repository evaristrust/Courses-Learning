import pandas as pd
import walter
from walter import df_frame
from creditout import total_credits
from creditout import cred_action
"""
columns:  'time_stamp', 'action', 'payer_name', 'credit_balance', 'total_repay'
"""
#Study of credits given out
#Notify based on the maximum credit set


cred_paid_df = df_frame.loc[:, [ 'time_stamp', 'action', 'payer_name', 'credit_balance', 'total_repay']]

#analyse the purchase (Kurangura)
cred_paid_action = cred_paid_df[cred_paid_df['action'] == 'Kwishyura ideni'].reset_index(0)

#check if I can change the dtype in total purchase from object to int
repaid_col = cred_paid_action['total_repay']
repaid_col = pd.to_numeric(repaid_col)

#Get the total business credit on products
total_credits_repaid = repaid_col.sum()

#create a function to allow more credit
def allow_cred():
    max_credit = 10000
    unpaid_credit = total_credits - total_credits_repaid # difference btn credits and repaid credit (balance)
    absolute_extra = abs(max_credit - unpaid_credit)
    if unpaid_credit < max_credit:
        print('You are allowed to give credits of no more than {}RWF'.format(absolute_extra))
    else:
        print('No, you can\'t give credits... Reached maximum with extra amount of {}RWF'.format(absolute_extra))
    print('Your unpaid credit is {}RWF'.format(unpaid_credit))

allow_cred()

#Group the credits owners with their credits, paid, and balance and sort them in descending
print('--'*20,'TOTAL CREDITS BY DEBTOR NAMES','--'*20)
debtors = cred_action.groupby('debtor_name')['product_cred_total'].sum()
print(debtors.sort_values(ascending=False)) #total credits by names

print('\n','--'*20,'TOTAL PAYMENT BY DEBTOR NAMES','--'*20)
debt_payers = cred_paid_action.groupby('payer_name')['total_repay'].sum()
print(debt_payers.sort_values(ascending=False)) #total payment by names sorted in desc order

#check chapati in debtors' name [not sure if this is someone's name hhaha]
# s = debtors_df[debtors_df['debtor_name'] == 'Chapati']
# print(s.loc[:, ['time_stamp','debtor_name', 'product_cred_total', 'product_credited']])
