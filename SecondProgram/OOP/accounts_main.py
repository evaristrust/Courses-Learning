class Account:
    """Creating an acount with name"""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("The account created for", self.name)

    def deposit(self, amount):
        if amount > 0:
            print("You deposited {}".format(amount))
            self.balance += amount
            self.show_balance()
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            print("You withdrew {}".format(amount))
            self.balance -= amount
            self.show_balance()
        else:
            print("OOps! You don't have that balance! You need to top up at least {} "
                  "to proceed".format(amount - self.balance))
            self.show_balance()

    def show_balance(self):
        print("Your balance is {}".format(self.balance))

if __name__ == '__main__': # Is this a buildin crap?
    full_name = Account("Evariste", 0)
    full_name.deposit(5000)
    full_name.withdraw(6000)
