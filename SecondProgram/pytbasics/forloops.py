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

# for i in range(1, 13):
#     for j in range(1, 5):
#         print("{0} times {1} is {2}".format(i, j, i*j))
#     print("====================")

# for i in range(1, 13):
#     for j in range(1, 5):
#         print("{0} times {1} is {2}".format(i, j, i * j), end="\t")
#     print("")