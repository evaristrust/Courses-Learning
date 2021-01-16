# #we are going to find factorials of numbers using for loop
def find_fact(n):
    results = 1
    if n > 1:
        for f in range(2, n + 1):
            results *= f
    return results

# for i in range(20):
#     print(i, ":", find_fact(i))
user_input = int(input("Your number here: "))
print(find_fact(user_input))




































