#
# my_list = list(range(10))
#
# odd = list(range(1, 10, 2))
# even = list(range(0, 10, 2))
#
# print(odd)
# print(even)
#
# # find an index of a string or an item
#
# small_elements = "efadadfedallidaldaheioisad"
#
# print(small_elements.index("l"))
# print(small_elements[10])
#
# # printout the odd numbers between 10 and 1000
# my_numbers = range(11, 10000, 2)
# print(my_numbers[932])
# for i in my_numbers:
#     print(i)
#
# # from 7 to 1000, check if the input is divisible by 7 or it's multiple of 7
#
# my_range = range(7, 1000, 7)
#
# my_input = int(input("Enter your number here and see if it's * of 7: "))
#
# my_calculation = my_input / 7
#
# if my_input in my_range:
#     print("{} is divisible by seven! {} divided by 7 is {} ".format(my_input, my_input, my_calculation))
# else:
#     print("{} is not divisible by 7. The reminder is {}".format(my_input, my_input % 7))

# another way of setting up things// range

initial_range = range(0, 10)
my_range = initial_range[::2]
print(my_range)
print(my_range[4])
for x in my_range:
    print(x)

decimals = range(0, 100)

range_one = decimals[3:40:3]
print(range_one)

# simply
print(range_one == range(3, 40, 3))
# should return true
# why should this turn true?

print(range_one == range(3, 41, 3))

list1 = range(0, 100)
for i in list1[::2]:
    print(i)

# for instance, let's get reverse the sentence

sentence = "dlrow eht ni segaugnal tseixes eht fo eno si nohtyP"

reverse_sentence = sentence[::-1]
print(reverse_sentence)