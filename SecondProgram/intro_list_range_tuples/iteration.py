
string = "0123456789"

# for i in string:
#     print(i)

# iterations: See how the iteration is done

# my_iteration = iter(string)
# print(my_iteration)
# print(next(my_iteration))
# print(next(my_iteration))
# print(next(my_iteration))
# print(next(my_iteration))
# print(next(my_iteration))
# print(next(my_iteration))
# print(next(my_iteration))
# print(next(my_iteration))
# print(next(my_iteration))
# print(next(my_iteration))
# print(next(my_iteration))

#
# for char in string:
#     print(char)
# for char in iter(string):
#     print(char)

my_new_iteration = iter(string)

for x in my_new_iteration:
    print(x)