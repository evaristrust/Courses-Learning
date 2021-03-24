# class Account:
#     """Creating an acount with name"""
#     """Creating a static method _current_time"""
#
#     def __init__(self, name: str, balance: float = 0.0):
#         self._name = name
#         self._balance = balance
#         print("The account created for", self._name)
#         self.show_balance()
#
#     def deposit(self, amount: float) -> float:  # creating a deposit method
#         if amount > 0:
#             print("{} has been deposited on {}'s Account".format(amount, self._name))
#             self._balance += amount
#             self.show_balance()
#
#     def withdraw(self, amount: float) -> float:
#         if 0.0 < amount <= self._balance:
#             print("{} is withdrawn from {}'s Account".format(amount, self._name))
#             self._balance -= amount
#             self.show_balance()
#         else:
#             print("OOps! You don't have that balance! You need to top up at least {} "
#                   "to proceed".format(amount - self._balance))
#             self.show_balance()
#
#     def show_balance(self):  # a method that will display the balance
#         print("Your balance is {}".format(self._balance))
#
#
# if __name__ == '__main__':
#     peter = Account("Peter", 0.0)
#     peter.deposit(10.1)
#     peter.deposit(0.2)
#     peter.withdraw(0.3)
