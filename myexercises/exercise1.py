# We are here going to work on the addition and multiplication
# Generate two digit integers and do their multiplication

# If their product is greater 1000, generate their sum , else generate their product
import random

num1 = random.randrange(10,100)
num2 = random.randrange(10,100)
product = num1 * num2
sum = num1 + num2

if product >=1000:
    print("The sum of ", num1, "and ", num2, "is ", sum)
else:
    print("The product of ", num1, "and ", num2, "is ", product)


# going to do the same exercises

# Find two random numbers from 1 to 20, add them and if their sum is greater than 12, do product

numa = random.randrange(1, 20)
numb = random.randrange(1, 20)

product = numa * numb
sum = numa + numb

if sum >= 12:
    print("The sum ", numa, "and", numb, "is greater or equal to 12; thus the product is: ", product)
else:
    print("The sum is less than 12, and it is: ", sum, ": addition of ", numa, "and", numb)