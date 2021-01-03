# i = 1
# for i in range(1,20):
#     print(i)
# 2222. now pint out the separate digits of 130340494049440404u404u04u04899

# num = "130340494049440404u404u04u04899"
# for i in range(0, len(num)):
#     # print(num[i])
#     print(num[i], end="\n")

# let's say that you've got so many data separated by a comma but u wanna remove them

# num = "130,34,049,404,9,44,04,04,u4,04,u04,u04,899"
# for i in range(0,len(num)):
#     if num[i] in "0123456789":
#         print(num[i], end="")

# num = "130,34,049,404,9,44,04,04,u4,04,u04,u04,899"
# cleanNumber = ""
# for i in range(0,len(num)):
#     if num[i] in "0123456789":
#         cleanNumber = cleanNumber + num[i]
#
# newNumber = int(cleanNumber)
# print("The number is {}".format(newNumber))

# Try the above with a new approach and use augmented operator assignment

number = "130,34,049,404,9,44,04,04,u4,04,u04,u04,899"
cleanedNumber = ""
for char in number:
    if char in "0123456789":
        cleanedNumber += char

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

# let's see for a list
#
# myList = ["Jesus", "Heaven", "Hell", "World", "God"]
#
# for grace in myList:
#     print("Find grace in", grace)
#
# for i in range(0, 100, 5):
#     print("This is: {}".format(i))

# let's nest loops ! like do calculations of two array elements!

for i in range(1, 13):
    for j in range(1, 5):
        print("{} times {} is {}".format(i, j, i*j))
    print("====================")

# for i in range(1, 13):
#     for j in range(1, 5):
#         print("{0} times {1} is {2}".format(i, j, i * j), end="\t")
#     print("")

# print numbers in styles like a triangle

largest_number = 10

for row in range(0, largest_number):
    for column in range(1, row + 1):
        print(column, end=' ')
    print('')

#print the sum of the numbers between 0 and 10! 10 included
print(".." * 40)
sum1 = 0

for i in range(11):
    sum1 += i

print("The sum is {} ".format(sum1))

# Ask the user to find the sum of the numbers from 0 and his prefered number
# user_number = int(input("Find the sum of numbers from 0 and your prefered number: "))
#
# sum2 = 0
#
# for w in range(user_number +1):
#     sum2 += w
#
# print("The sum of numbers from 0 and {} is {} ".format(w, sum2))

# Ask the user to see the multiplication table of any number

print("We are going to find the multiplication table of your number")
your_number = int(input("Enter your number here: "))

for num in range(13):
    print("{} times {} is {} ".format(your_number, num, your_number * num))

# Printing a sex pattern but from the above numbers

n = 10
k = 10

for i in range(0, n + 1):
    for j in range(k-i, 0, -1):
        print(j, end=' ')
    print()

# Going to print the prime numbers from 1 to 100

start = 1
end = 100

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)