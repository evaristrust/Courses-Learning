# print the fibanacci sequences for one to 20
# fibonacci is a sequence that takes the previous number
# number and adds to the current to obtain the next
# number

highest = int(input("Put a nber and get it's fibonacci: "))
count = 0
num1, num2 = 0, 1
print("The fibanacci sequence up to {} is:".format(highest))
while count < highest:
    print(num1, end=" ")
    total = num1 + num2
    num1 = num2
    num2 = total
    count += 1
