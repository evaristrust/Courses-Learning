# # Let's do something!! Are you ready to drink?
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

# Now let's play a game of guessing numbers

print("Guess a number between 1 and 10: ")
guess = int(input())
if guess == 5:
    print("Wowww! You guessed it on the first time!!")
elif guess > 5:
    print("Guess lower")
    guess = int(input())
    if guess == 5:
        print("You guessed it!BOOM")
    else:
        print("Sorry, you didn't guess correctly")
elif guess < 5:
    print("Guess higher")
    guess = int(input())
    if guess == 5:
        print("You guessed it!BOOM")
    else:
        print("Sorry, you didn't guess correctly")


