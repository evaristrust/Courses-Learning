# # Create a small program that takes an ip address at the keyboard
# # and prints out the number of segments it contains, and the length of each segment.
# # An IP address consists of 4 numbers, separated by each other with a period
#
# ip_address = input("Enter you IP address: ")
# segment = 1
# segment_length = 0
# character = ""
# # each time we find a period in the input string
# # We are going to increment a counter of how many segments
# # there now unless the input is blank
# # there will always be at least one segment
# # that's y we initiated segmennt at 1
# # we are going to also count how many characters in each segment
# # then let's check if we got a fullstop or period
# # if we find a period, we will end the segment and start a new one
#
# for character in ip_address:
#     if character == ".":
#         print("The segment {} contains {} characters".format(segment, segment_length))
#         segment += 1
#         segment_length = 0
#     else:
#         segment_length += 1
#
# # unless the last character is equal to period, we shouldn't have printed the last segment
# # this is because we told the program to teminate when it finds a period
# # that's why we have missed the last segment in the output
#
# if character != ".":
#     print("The segment {} contains {} characters".format(segment, segment_length))

# There are many ways to solve a challenge
ip_address = input("Enter you IP address: An IP address consists of 4 numbers,"
                   " separated by each other with a period ")
segment = 1
segment_length = 0
if ip_address[-1] != ".":
    ip_address += "."

for character in ip_address:
    if character == ".":
        print("The segment {} contains {} characters".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1