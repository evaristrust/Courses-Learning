"""Imma start playing with factorial of a number
and you will probably enjoy how i started """


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


# Going to find the factorial of a number
# Going to print the responses
# check the condition that the factorial exists

num = int(7)

if num < 0:
    print("There is no factorial of a negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of ", num, "is: ", factorial(num))


# give it a try and input number by a user

def find_factorial(num):
    if num == 1:
        return num
    else:
        return num * find_factorial(num-1)

# work around on the factorial!
input_number = int(input("Put any number and see the factorial of it!\n"))

if input_number < 0:
    print("{} does not have any factorial since it is negative".format(input_number))
elif input_number == 0:
    print("The factorial of {} is 1".format(input_number))
else:
    print("The factorialof {} is {}".format(input_number, find_factorial(input_number)))