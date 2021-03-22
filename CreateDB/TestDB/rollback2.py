import sqlite3

"""The modification in this codes from rollback1 is the {:.1f}
    just to avoid an error of floating in the end results and inexact amount"""

db = sqlite3.connect("accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts(name TEXT PRIMARY KEY NOT NULL,"
           " balance INTEGER NOT NULL)") #Accounts table
db.execute("CREATE TABLE IF NOT EXISTS history(time TIMESTAMP NOT NULL, account TEXT NOT NULL, "
           "amount INTEGER NOT NULL, PRIMARY KEY(time, account))")

class Account:
    """Creating an acount with name"""
    """Creating a static method _current_time"""

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

    def deposit(self, amount: int) -> float:  # creating a deposit method
        if amount > 0:
            print("{:.1f} has been deposited on {}'s Account".format(amount, self._name))
            self._balance += amount
            self.show_balance()

    def withdraw(self, amount: int) -> float:
        if 0.0 < amount <= self._balance:
            print("{:.1f} is withdrawn from {}'s Account".format(amount, self._name))
            self._balance -= amount
            self.show_balance()
        else:
            print("OOps! You don't have that balance! You need to top up at least {} "
                  "to proceed".format(amount - self._balance))
            self.show_balance()

    def show_balance(self):  # a method that will display the balance
        print("The balance on {}'s account is {:.1f}".format(self._name, self._balance))


if __name__ == '__main__':
    peter = Account("Peter")
    peter.deposit(10.1)
    peter.deposit(0.2)
    peter.withdraw(0.3)

    print("-" * 40)

    evariste = Account("Evariste")
    evariste.deposit(20.1)
    evariste.deposit(0.4)
    evariste.withdraw(1.2)

    print("-" * 40)
    jeanne = Account("Jeanne")
    dianah = Account("Dianah", 100)
    octave = Account("Octave", 300)
    alex = Account("Alex")
