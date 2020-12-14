import os
import sys

# learning the functions:
# First example of function
def my_function(name, age, food,
                height, sports,
                hobby, month, year):
    print("This is the first function")

# Second example of user defined function
def second_function():
    print("This is the second function")


my_function("me", 22, "rice",
            1.8, "soccer",
            "Jogging", "March", 2020)
second_function()

# check something if it's true or not!
check = True
if check is True:
    print("it is true")
