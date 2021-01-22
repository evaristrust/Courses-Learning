class Account:
    """Creating an acount with name"""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print('The account created for', self.name)
        print('d= deposit; w= withdraw; c= check balance; q= quit')

    def deposit(self, amount):
        amount = int(input('How much? '))
        if amount > 0:
            print('You deposited {}'.format(amount))
            self.balance += amount
            self.show_balance()
    def withdraw(self, amount):
        amount = int(input('How much? '))
        if 0 < amount <= self.balance:
            print('You withdrew {}'.format(amount))
            self.balance -= amount
            self.show_balance()
        else:
            print('OOps! You don\'t have that balance! You need to top up {} '
                  'to proceed'.format(amount - self.balance))
            self.show_balance()

    def show_balance(self):
        print('Your balance is {}'.format(self.balance))

if __name__ == '__main__': # Is this a buildin crap?
    full_name = Account('Evariste', 5000)
    # down there i was trying to ask a user!
while full_name:
    user = input('Choose an action: d, c, q or w? ')
    if user == 'd':
        full_name.deposit(0)
        # user = input("Choose an action: d, c, q or w? ") # added this just to reappear when a
    elif user == 'w':
        full_name.withdraw(0)
    elif user == 'c':
        full_name.show_balance()
    elif user == 'q':
        print('That you for using Valva service!')
        break
        user = input('Choose an action: d, c, q or w? ')
    else:
        print('sorry, we don\'t have that option')
