import datetime
import pytz


class Account:
    """Creating an acount with name"""
    """Creating a static method _current_time"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = []
        print("The account created for", self._name)

    def deposit(self, amount):
        if amount > 0:
            print("You deposited {}".format(amount))
            self._balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            self._transaction_list.append((Account._current_time(), amount)) # simplifying with the static method
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            print("You withdrew {}".format(amount))
            self._balance -= amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("OOps! You don't have that balance! You need to top up at least {} "
                  "to proceed".format(amount - self._balance))
            self.show_balance()
    def show_balance(self):
        print("Your balance is {}".format(self._balance))
    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = 'deposited'
            else:
                trans_type = 'withdrawn'
                amount *= -1
            print('{:6} {} on {} (local time was {})'.format(amount, trans_type, date, date.astimezone()))

if __name__ == '__main__': # Is this a buildin crap?
    full_name = Account("Evariste", 5000)
    full_name.deposit(5000)
    full_name.withdraw(2000)
    full_name.show_transaction()
    print('**'* 40)
    full_name1 = Account("Joe", 0)
    full_name1.deposit(5000)
    full_name1.withdraw(2000)
    full_name1.show_transaction()

# stopped and finished the vid 6.. will immediately start vid 7
