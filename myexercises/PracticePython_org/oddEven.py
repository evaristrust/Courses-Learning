# Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user.

# Extras:
#
#     If the number is a multiple of 4, print out a different message.
#     Ask the user for two numbers: one number to check (call it num)
#     and one number to divide by (check).
#     If check divides evenly into num,
#     tell that to the user. If not, print a different appropriate message.

number = int(input("Put any number here and I will let you know"
                "if it's odd or even\n"))
if number % 4 == 0:
    print("{} the multiple of 4".format(number))
elif number % 2 == 0:
    print("{} is even!".format(number))
else:
    print("{} is odd!".format(number))

num = int(input("Enter any number here: "))
check = int(input("Enter any other number here: "))

if num % check == 0:
    print("{} divides evenly into {}".format(check, num))
else:
    print("{} does not divide evenly into {}".format(check, num))