import random
import keyboard

low, high, guess, attempts, max_attempts = 1, 100, 0, 1, 5
result = random.randint(low, high)
print('choose an integer between {0} and {1}'.format(low, high))

while guess != result:
    guess = int(input())
    if guess == 0 | guess > high:
        break
    elif attempts >= max_attempts:
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
