# we are going to see the equivalence of the decimal numbers from 0 to 20 with binary system

for i in range(21):
    print("{0:>2} in binary is: {0:>08b}".format(i))
# do a program that asks a user to put a number and then see the
# the binary system of the inputted number

my_number = int(input("Put any decimal number here: "))
print("The binary format of {0:>2} is {0:>08b}".format(my_number))
