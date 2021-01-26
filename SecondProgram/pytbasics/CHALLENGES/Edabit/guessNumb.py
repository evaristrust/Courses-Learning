# We are going to test something
# play the game of choosing higher or lower

# initialize variables max_number, guess, trials, random_number
import random
max_number = 20
guess = 0
trials = 1
random_number = random.randint(1, max_number)
print('Choose a number between 1 and 20: ')
while guess != random_number:
    guess = int(input())
    if guess == 0 or guess > max_number:
        print('You chose 0 or a number higher than the maximum')
        break20
    if trials > 6:
        print('You are allowed no more than 6 attempts')
        break
    if guess > random_number:
        print('choose lower')
    elif guess < random_number:
        print('choose higher')
    else:
        print('You guessed it man!')
    trials += 1
