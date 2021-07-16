import random
import keyboard
#GAME OVERVIEW:
'''
choose a random int number between two shown numbers on the screen
the computer will generate a random number too
it will alert you if you guessed it or ask you to choose higher or lower
you will do so until you guessed it, but it will stop you when the max number
of attempts are reached.
when you input 0 or number higher than the maximum,
it will break or stop! good luck !!!
'''
#low: the minimum number in the range
#high: the max number in the range
#guess: the user input
#attempts: the initial number of attempts
#max_attempts: the maximum number of attempts or trials
low, high, guess, attempts, max_attempts = 1, 100, 0, 1, 5
result = random.randint(low, high)
print('choose an integer between {0} and {1}'.format(low, high))

while guess != result:
    guess = int(input())
    if guess == 0 | guess > high:
        break
    elif attempts > max_attempts:
        print('FAILED! maximum attempts reached!')
        break
    elif guess < result:
        print('choose higher')
    elif guess > result:
        print('choose lower')
    elif guess == result:
        print('YOU WON, CONGRATS!')
    else:
        print('BOOM BOOM BOOM, CONGRATULATIONS!')
    attempts += 1
