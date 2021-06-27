# release multiply of 5 numbers from 0 and 100
print('MULTIPLES OF FIVE:')
count = 1
for i in range(5, 100, 5):
    print("No.{} is {}".format(count, i))
    count += 1

# find the product of odd numbers and even numbers from 0 to 20
# DisplayFashion: show the NO.1 product is btn {} and {}. Equals to {}
print('--'*40)
print('MULTIPLICATION TABLE:')
numbered = 1
for x in range(1, 20, 2):
    for y in range(2, 20,2):
        print("N0.{} product is between {} and {} = {}".format(numbered, x, y, x * y))
        numbered += 1

print('--'*40)
print('Get whether a boolen variable is True:')
y = False
if y:
    print("It's true!")
else:
    print("It's False!")

# print the prime number from 1 and 200
print('--'*40)
print('Get Prime numbers between 1 and 200:')
start = 1
end = 200
orders = 1
for num in range(start, end +1):
    if num > 1: # all the numbers should be greater than 1
        for x in range(2, num): #two is a prime number
            if num % x == 0:
                break
        else:
            print('Prime {} is: {}'.format(orders, num))
        orders += 1

# print fibonacci sequences
print('--'*40)
print('GET FIBONACCI NUMBERS:')
terms = 20 #number of fibonaccis
num1, num2 = 0, 1
count = 1
while count < terms:
    print('NO.{}: {}'.format(count,num1), end= "\n")
    total = num1 + num2
    num1 = num2
    num2 = total
    count += 1
