# choose a number between 1 and 20
# if a player choose 0, break the loop
# keep asking the player to choose until they get it right
# if they get it, break the loop

import random

print("Choose a number between 1 and 20")
max_number = 20
number = random.randint(1,max_number)
guess = 0
while guess != number:
    guess = int(input())
    if guess == 0 or guess > max_number:
        break
    if guess < number:
        print("choose higher")
    elif guess > number:
        print("choose lower")
    else:
        print("You chose the right number")

# Support the max_number is 10000! and I want to stop the loop at the 10th guess
# Which coding can i do to make this wish??
