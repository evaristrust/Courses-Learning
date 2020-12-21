# Create program that shows numbers in the range of 10
# show the previous number and current one
# show also the sum of the previous and current number

print("\n""The output of the first practical exercise:""\n")
def release_num(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("previous is: ", previousNum, "current is: ", i, "sum is: ", sum)
        previousNum = i

release_num(10)


print("\n""======================================================" "\n")
# same exercises: revision
print("\n""The output of the second practical exercise:""\n")
def print_numbers(numb):
 # generate previous number and the sum between current and previous number
    previous_number = 0
    for y in range(numb):
        sum = previous_number + y
        print("The current number is: ",y, "\n""The previous number is: ",
          previous_number, "\n""The sum is: ", sum)
        previous_number = y
print_numbers(10)













