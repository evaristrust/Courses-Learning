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
