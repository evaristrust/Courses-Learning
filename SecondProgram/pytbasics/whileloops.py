# While loop check evaluates condition and stops when the condition is false!
# print the odd numbers between 0 and 20 using both for and while loops

# for loop
print('FOR_LOOPS / OLD NUMBERS BETWEEN 0 AND 30:')
for i in range(1, 20, 2):
    print("The number {} is odd".format(i))

# while
print('--'*40)
print('WHILE_LOOPS / OLD NUMBERS BETWEEN 0 AND 30:')
x = 1
while x <= 20:
    print("The number {} is odd".format(x))
    x += 2

# guess the number between 1 and 10
import random

highest = 10
answer = random.randint(1, highest)

print("Please enter and number between 1 and {}\n".format(highest))
guess = 0
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
    print("You have guessed it for the first time!")
