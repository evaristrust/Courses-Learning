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
    def withdraw(self, amount):
        if amount > 0:
            print("You withdrew {}".format(amount))
            self.balance -= amount
    def show_balance(self):
        print("Your balance is {}".format(self.balance))
if __name__ == '__main__':
    full_name = Account("Evariste", 0)
    full_name.show_balance()
    full_name.deposit(5000)
    full_name.show_balance()
    full_name.withdraw(2300)
    full_name.show_balance()
