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

# Give students scholarships depending on the range of their grades
# a student above or equal 90 will get full scholarship
# above 80 will get a partial scholarship
# above 70 will get free tuition
name = input("What is your name dear: ")
grades = int(input("Hi {}! what was your final grade? ".format(name) ))

if 90 < grades <= 100:
    print("You have a full scholarship")
elif 80 < grades <= 90:
    print("You have a partial scholarship")
elif 70 < grades <= 80:
    print("You will not pay tuition fee but you full support your on the living costs")
else:
    print("You will pay every costs related to your study")