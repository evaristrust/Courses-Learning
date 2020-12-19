# While loop check evaluates condition and stops when the condition is false!
# print the odd numbers between 0 and 20 using both for and while loops

# for loop
#
# for i in range(1, 20, 2):
#     print("The number {} is odd".format(i))

# while

# x = 1
#
# while x <= 20:
#     print("The number {} is odd".format(x))
#     x += 2

# Let's say you in a hall and you want to go out!
#
# available_exits = ["North", "East", "South east", " North East", " West"]
#
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Choose direction again: ")
#
# print("Go ahead and pass through {}".format(chosen_exit))

# you can also use break and else in while looop
# available_exits = ["North", "East", "South east", " North East", " West"]
#
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Choose direction again: ")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
# else:
#     print("Go ahead and pass through {}".format(chosen_exit))

# simple game without using a while loop and we will get back to it

# guess the number between 1 and 10

import random

highest = 10
answer = random.randint(1, highest)

print("Please enter and number between 1 and {}".format(highest))
guess = 0
# first check if the guessed number is not answer
# if guess != answer:
#     if guess < answer:
#         print("choose higher")
#     else:
#         print("choose lower")
#     guess = int(input())
#     if guess == answer:
#         print("The random generated number is {} and you choose {}"
#               "there you guessed it".format(answer, guess))
#     else:
#         print("You did not choose correctly")
#
# else:
#     print("You guessed it for the first time "
#           "The random generated number is {} and you choose {} "
#               "there you guessed it".format(answer, guess))

# you can see that the loop is stopping at two guessed! here is where the while loop is so important
# we are going to do the same example as above but we will break the loop if a player input 0 (zero)
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("guess higher")
    elif guess > answer:
        print("guess lower")
    else:
        print("You guessed it thanks!")



