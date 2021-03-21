n = int(input("Enter your number here: "))
def factorial(n):
    """n! is also defined as n * (n-1)!"""
    if n < 0:
        return "There is no factorial for such number"
    elif n <= 1:
        return 1
    else:
        return n * factorial(n-1)
try:
    print(factorial(n))
except RecursionError: # Error that occurs when the program runs out of the memory in the recursion
    print("The program can't print such large values")

print("The program terminated!")
