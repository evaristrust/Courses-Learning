# we are going to see the equivalence of the decimal numbers from 0 to 20 with binary system
import random
for i in range(21):
    print("{0:>2} in binary is: {0:>08b}".format(i))
# do a program that asks a user to put a number and then see the
# the binary system of the inputted number
#
# my_number = int(input("Put any decimal number here: "))
# print("The binary format of {0:>2} is {0:>08b}".format(my_number))

# How about finding the number in hex
for i in range(21):
    print("{0:>2} in hex is: {0:>02x}".format(i))

# let's do some operations in hex

x = 0x0a
y = 0x0d
p = x * y
print(p)

print("**" * 40)

for num in range(10):
    print("{0:>2} in binary is equal to {0:>08b}".format(num))
print("**" * 40)
for hex in range(10):
    print("{0:>2} in hex is {0:>02x}".format(hex))

#using function to find this!

print("??" * 40)
def binary(num):
    print("{0:>2} equals to {0:>08b} in binary".format(num))

binary(1)