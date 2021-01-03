# choose a number between 1 and 20
# if a player choose 0, break the loop
# keep asking the player to choose until they get it right
# if they get it, break the loop
#
# import random
# # initiate variables, max, guess, trials, and the range for the number guesses
# print("Choose a number between 1 and 20 ")
# max_number = 20
# number = random.randint(1,max_number)
# guess = 0
# trials = 1 # initializing a varibale that will increment to check the max trials
# while guess != number:
#     guess = int(input())
#     if guess == 0 or guess > max_number:
#         break
#     if trials > 5:
#         print("You are allowed only 5 attempts")
#         break
#     if guess < number:
#         print("choose higher")
#     elif guess > number:
#         print("choose lower")
#     else:
#         print("You chose the right number")
#     trials += 1

# release multiply of 5 numbers from 0 and 100

# count = 1
# for i in range(5, 100, 5):
#     print("No.{} is {}".format(count, i))
#     count += 1
# find the product of odd numbers and even numbers from 0 to 20
# show the NO.1 product is btn {} and {}. Equals to {}

# numbered = 1
#
# for x in range(1, 20, 2):
#     for y in range(2, 20,2):
#         print("N0.{} product is between {} and {} = {}".format(numbered, x, y, x * y))
#         numbered += 1
#     print("**" * 40)

# We are going to test something
# play the game of choosing higher or lower

# initialize variables max_number, guess, trials, random_number
# import random
# max_number = 20
# guess = 0
# trials = 1
# random_number = random.randint(1, max_number)
# print('Choose a number between 1 and 20: ')
# while guess != random_number:
#     guess = int(input())
#     if guess == 0 or guess > max_number:
#         print('You chose 0 or a number higher than the maximum')
#         break
#     if trials > 6:
#         print('You are allowed no more than 6 attempts')
#         break
#     if guess > random_number:
#         print('choose lower')
#     elif guess < random_number:
#         print('choose higher')
#     else:
#         print('You guessed it man!')
#     trials += 1
#

y = False
if y:
    print("It's true!")
else:
    print("It's False!")




# print the prime number from 1 and 200

start = 1

end = 200

for num in range(start, end +1):
    if num > 1: # all the numbers should be greater than 1
        for x in range(2, num):
            if num % x == 0:
                break
        else:
            print(num)

# print fibonacci sequences

terms = 10

num1, num2 = 0, 1
count = 0
print('fibonacci sequence: ')
while count < terms:
    print(num1, end=' ')
    total = num1 + num2
    num1 = num2
    num2 = total
    count += 1







