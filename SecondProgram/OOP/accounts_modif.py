import datetime
import pytz
class Account:
    """Creating an account with name"""
    """create a static method _current_time"""
    @staticmethod # just modified to help in line 25 and 32 .. self._transaction_list = [(Account._current_time(), balance)]
    # jut to simply the codes lines... pytz.utc.localize(datetime.datetime.utcnow())

    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print('The account created for', self._name)
        print('d= deposit; w= withdraw; c= check balance; q= quit; and t to check the transaction')

    def deposit(self, amount):
        amount = int(input('How much? '))
        if amount > 0:
            print('You deposited {}'.format(amount))
            self._balance += amount
            self.show_balance() # after deposit, show the balance..new balance
            self._transaction_list.append((Account._current_time(), amount))
    def withdraw(self, amount):
        amount = int(input('How much? '))
        if 0 < amount <= self._balance:
            print('You withdrew {}'.format(amount))
            self._balance -= amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print('OOps! You don\'t have that balance! You need to top up at least {} '
                  'to proceed'.format(amount - self._balance))
            self.show_balance()

    def show_balance(self):
        print('Your balance is {}'.format(self._balance))

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = 'deposited'
            else:
                trans_type = 'withdrawn'
                amount *= -1
            print('{:6} {} on {} (local time was {})'.format(amount, trans_type, date, date.astimezone()))
            # you can remove the utc time just to be user friendly...
            # users need to see their local times. that's it.

if __name__ == '__main__': # so basically it is checking if you are running the file directly
    full_name = Account('Evariste', 5000)
    # down there i was trying to ask a user!
while full_name:
    user = input('Choose an action: d, c, q, w, t? ')
    if user == 'd':
        full_name.deposit(0)
    elif user == 'w':
        full_name.withdraw(0)
    elif user == 'c':
        full_name.show_balance()
    elif user == 't':
        full_name.show_transaction()
    elif user == 'q':
        print('That you for using our service!')
        break
        user = input('Choose an action: d, c, q, w, t? ')
    else:
        print('sorry, we don\'t have that option')

# Task: create other two accounts and run logics
# condition: Ask the user to put their names
# and then run their own accounts 
