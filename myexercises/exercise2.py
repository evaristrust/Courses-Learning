def release_num(num):
    previousNum = 0
    for i in range(num):
        sum = previousNum + i
        print("previous is: ", previousNum, "current is: ", i, "sum is: ", sum)
        previousNum = i

release_num(10)