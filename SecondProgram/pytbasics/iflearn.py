# # 1111. Let's do something!! Are you ready to drink?
# name = input("What's your name? ")
# age = int(input("How old are you, {}".format(name)))
#
# # Going to check your eligibility
#
# if age >= 18:
#     print("You are old enough to drink")
#     print("Go find any type of drink")
# else:
#     print("You are still young!!!" + "You will be eligible in {0} years".format(18-age))

# 222. Now let's play a game of guessing numbers

# print("Guess a number between 1 and 10: ")
# guess = int(input())
# if guess == 5:
#     print("Wowww! You guessed it on the first time!!")
# if guess > 5:
#     print("Guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("You guessed it!BOOM")
#     else:
#         print("Sorry, you didn't guess correctly")
# elif guess < 5:
#     print("Guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("You guessed it!BOOM")
#     else:
#         print("Sorry, you didn't guess correctly")
#
#
# else:
#     print("Wowww! You guessed it on the first time!!")

# 333. More on if elif else

# age = int(input("what's your age?\n"))
#
# # if (age >= 16) and (age <= 40):
# # the same as:
# if 16 < age <= 40:
#     print("You are less likely to contract covid19")
# else:
#     print("have a good day!")

# 444. If using Boolean data type

# x = True
# if x:
#     print("It is true")

# 555. You can also do the example #1111 using not if not

# name = input("What's your name? ")
# age = int(input("How old are you, {}".format(name)))
#
# # Going to check your eligibility
#
# if not age < 18:
#     print("You are old enough to drink")
#     print("Go find any type of drink")
# else:
#     print("You are still young!!!" + "You will be eligible in {0} years".format(18-age))

# 666.==============

# x = input("write something")
# if x:
#     print("You typed {}".format(x))
# else:
#     print("We did not hear you!")

# 777. another example

name = "Evariste"
letter = input("put letter: ")

if letter in name:
    print("The letter {} is here".format(letter))
else:
    print("I don't recognize {} in your name".format(letter))