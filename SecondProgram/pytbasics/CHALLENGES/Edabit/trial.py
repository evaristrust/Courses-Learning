my_list = [34, 23, 21, 64, 23, 63, 75, 45]
def my_largest(x, lst):
    my_list = lst
    sorted_lst = sorted(lst)
    return sorted_lst[len(lst)-x:]

print(my_largest(3, my_list))

champions = {"epl": "Arsenal, Chelsea, Man utd",
             "laliga": "Barcelona, Real Madrid, Atletico",
             "serie_a": "Juventus, Inter, Ac Milan"}

# while True:
#     check_teams = input("Enter your champion! ")
#     description = champions.get(check_teams)
#     if check_teams == 'quit':
#         break
#     elif check_teams in champions:
#         print(description)
#     else:
#         print("We didn't see your teams")

# create a program that:
# asks a user to guess a random number
# if the guess is 0 or above the range, break
# otherwise, ask them to choose higher or lower
# if correct, throw you are good
# import random
#
# print("Instructions: Type 0 to quit or a number to go on!\n")
# print("Choose a number between 1 and 20: ")
# answer = 0
# highest = 20
# max_trial = 1
# my_rand_number = random.randint(1, highest)
#
# while answer != my_rand_number:
#     answer = int(input())
#     if answer == 0:
#         break
#     elif answer > highest:
#         print("You put the number out of range")
#         break
#     elif max_trial > 5:
#         print("You are allowed 5 trials!")
#         break
#     elif answer < my_rand_number:
#         print("Choose higher!")
#     elif answer > my_rand_number:
#         print("Choose lower")
#     else:
#         print("Boom you got it man!")
#     max_trial += 1

# print the prime number from 0 and 100

# start = 0
# end = 100
# for num in range(start, end):
#     if num == int(num): # nbers need to be positive!
#         for x in range(2, num):
#             if num % x == 0:
#                 break
#         else:
#             print(num)

# ask a user to put a number
# check if that nber is a prime
# a prime an integer nber only divided by 1 and itself

num = int(input("Enter you number: "))
for x in range(2, num):
    if num % x == 0:
        print("It is not a prime")
        break
else:
    print("It is a prime")













