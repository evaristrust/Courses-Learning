# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("What is your name dear? ")
age = int(input("Dear {}, how old are you?".format(name)))

print("OOOh woww! You will turn 100 in {} years from now".format(100 - age))