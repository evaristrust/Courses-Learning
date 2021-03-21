"""do a program that asks a user to add two numbers
and then return the division between the first and the second.
Make sure the program behaves safe on the user-end, even control commands
"""
import sys

def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except EOFError: #The order of exceptions always matter
            sys.exit(1)
        except: # This should really be ValueError exception
            print("Invalid input was entered")
        finally:
            print("Finally clause is always executed")

first_number = get_int("Enter your first number ")
second_number = get_int("Enter your second number ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except (ZeroDivisionError, EOFError):
    print("Such division won't work")
    sys.exit(2)
else:
    print("The division has been successfully done")