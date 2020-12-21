# choose a number between 1 and 20
# if a player choose 0, break the loop
# keep asking the player to choose until they get it right
# if they get it, break the loop

import random
# initiate variables, max, guess, trials, and the range for the number guesses
print("Choose a number between 1 and 20")
max_number = 20
number = random.randint(1,max_number)
guess = 0
trials = 1
while guess != number:
    guess = int(input())
    if guess == 0 or guess > max_number or trials > 5:
        break
    if guess < number:
        print("choose higher")
    elif guess > number:
        print("choose lower")
    else:
        print("You chose the right number")
    trials += 1


# Support the max_number is 10000! and I want to stop the loop at the player's 10th guess
# Which coding can i do to make this wish?? I don't get how i can do it
