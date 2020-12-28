# Keyword: Pythonic: what is it... pythonic way of doing things
# use two slashes to specify the path in windows
# jabber = open("C:\\Users\\Evariste2020\\Desktop\\tech.txt", "r") # r is a module
#
# for line in jabber:
#     print(line)
# jabber.close()

# now that we can each by passing a condition
# whether it contains a certain word
#
# jabber = open("C:\\Users\\Evariste2020\\Desktop\\tech.txt", "r") # r is a module
#
# for line in jabber:
#     if "tek experts" in line.lower():
#         print(line, end="")
# jabber.close()

# wanna do this without using close()
# we will use with ... as
# with open("C:\\Users\\Evariste2020\\Desktop\\tech.txt", "r") as jabber:
#     for line in jabber:
#         if "PROJECT MANAGEMENT" in line.upper():
#             print(line, end="")


with open("C:\\Users\\Evariste2020\\Desktop\\tech.txt", "r") as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()
