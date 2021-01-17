# print the prime number from 0 and 100
#
# start = 0
# end = 100
# for num in range(start, end):
#     if num == int(num): # nbers need to be positive!
#         for x in range(2, num):
#             if num % x == 0:
#                 break
#         else:
#             print(num, end= " ")

my_number = int(input("Enter your number: "))
if my_number > 0: # loop the positive integers
    for x in range(2, my_number):
        if (my_number % x) == 0:
            print("It's not a prime number")
            break

    else:
        print("It's a prime number")
else: # 0 or a negative number isn't a prime
    print("it's less or equal to zero.. so not a prime")

