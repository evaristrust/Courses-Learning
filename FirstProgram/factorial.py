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
