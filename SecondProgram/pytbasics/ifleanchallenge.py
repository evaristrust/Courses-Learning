# write a small program to ask for a name and an age
# when both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be over 18 and under 31)
# if they are, welcome them to the holiday, otherwise print
# a polite message refusing their entry

# name = input("Enter your Name: ")
# age = int(input("Enter Your age: "))
#
# if 18 <= age < 31:
#     print("You are welcome to the holiday")
# else:
#     print("Sorry, you are not eligible for the holiday")

# Do it in an engaging way

name = input("What's your name dear? ")
age = int(input("Great! How are old you dear {} ".format(name)))
if 18 <= age < 31:
    print("We are pleased to welcome you to the holidays dear {}".format(name))
else:
    print("Sorry, We are unfornately unable to welcome you to the holidays")