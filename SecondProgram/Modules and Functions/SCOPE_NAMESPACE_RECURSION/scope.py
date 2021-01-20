# #we are going to find factorials of numbers using for loop
# we are going to learn recursion
# recursive function is a function that calls itself
def fact(x):
    result = 1
    for y in range(2, x + 1):
        if x > 1:
            result *= y
    return result

for r in range(20):
    print(r, fact(r))


# try it here!
def find_fact(n):
    results = 1
    if n > 1:
        for f in range(2, n + 1):
            results *= f
    return results
#
# for i in range(20):
#     print(i, ":", find_fact(i))
# user_input = int(input("Your number here: "))
# print(find_fact(user_input))

# another example of recursive function is fibonacci

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
for i in range(30):
    print(i, ": ",fib(i))
# you can see the recursion is slow

# do fibonacci without recursion, it will be faster
def fibonacci(x):
    if x == 0:
        result = 0
    elif x == 1:
        result = 1
    else:
        n_minus_1 = 1
        n_minus_2 = 0
        for f in range(1, x):
            result = n_minus_1 + n_minus_2
            n_minus_2 = n_minus_1
            n_minus_1 = result
    return result

for i in range(30):
    print(i, " : ", "\t", fibonacci(i))

















































