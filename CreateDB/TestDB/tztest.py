import sqlite3
import pytz
import datetime
import pickle
"""The modification in this codes from rollback1 is the {:.2f}
    just to avoid an error of floating in the end results and inexact amount"""

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts(name TEXT PRIMARY KEY NOT NULL,"
           " balance INTEGER NOT NULL)") #Accounts table
db.execute("CREATE TABLE IF NOT EXISTS histories(time TIMESTAMP NOT NULL, account TEXT NOT NULL,"
           "amount INTEGER NOT NULL, zone INTEGER NOT NULL, PRIMARY KEY(time, account))")
#create a view from histories
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS "
           "SELECT strftime('%Y-%m-%d %H:%M:%f', histories.time, 'localtime') AS localtime,"
           "histories.account, histories.amount FROM histories ORDER BY histories.time")

class Account:
    """Creating an acount with name"""
    @staticmethod
    def _current_time():
        #return pytz.utc.localize(datetime.datetime.utcnow())
        utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo
        return utc_time, zone

    def __init__(self, name: str, balance: int = 0):

        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self._name, self._balance = row
            print("Data retrieved for {}.".format(self._name), end=" ")
        else:
            self._name = name
            self._balance = balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, balance))
            cursor.connection.commit()
            print("The account created for {}".format(self._name))
        self.show_balance()

    def save_update(self, amount): # Created this to save the identical codes in deposit and withraw (commented)
        new_balance = self._balance + amount
        deposit_time, zone = Account._current_time() #<-- unpack returned turple
        pickled_zone = pickle.dumps(zone)
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self._name))
        db.execute("INSERT INTO histories VALUES(?, ?, ?, ?)", (deposit_time, self._name, amount, pickled_zone))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:  # creating a deposit method
        if amount > 0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)",(new_balance, self._name))
            # db.execute("INSERT INTO histories VALUES(?, ?, ?)", (deposit_time, self._name, amount))
            # db.commit()
            # self._balance = new_balance
            self.save_update(amount)
            print("{:.2f} has been deposited on {}'s Account".format(amount / 100, self._name))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0.0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withraw_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self._name))
            # db.execute("INSERT INTO histories VALUES(?, ?, ?)", (withraw_time, self._name, -amount))
            # db.commit()
            # self._balance
            self.save_update(-amount)
            print("{:.2f} is withdrawn from {}'s Account".format(amount / 100, self._name))
            return amount / 100
        else:
            print("THE AMOUNT HAS TO BE BETWEEN ZERO AND YOUR BALANCE")
            return 0.0

    def show_balance(self):  # a method that will display the balance
        print("The balance on {}'s account is {:.2f}".format(self._name, self._balance / 100))


if __name__ == '__main__':
    peter = Account("Peter")
    peter.deposit(1010)
    peter.deposit(20)
    peter.withdraw(30)

    print("-" * 40)

    vavic = Account("Evariste")
    vavic.deposit(2010)
    vavic.deposit(40)
    vavic.withdraw(120)

    print("-" * 40)
    jeanne = Account("Jeanne")
    dianah = Account("Dianah", 100)
    octave = Account("Octave", 300)
    alex = Account("Alex")
    donny = Account("Donny", 500)

    db.close()
