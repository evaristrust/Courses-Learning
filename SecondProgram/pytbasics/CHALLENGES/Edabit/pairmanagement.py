#Given two arguments,
# return a list which contains these two arguments.

def my_arg(a, b):
    my_list = a, b
    new_list = list(my_list)
    return new_list

print(my_arg(1, 2))

# or

def my_nums(num1, num2):
    return [num1, num2] # but for long list, it's not efficient

print(my_nums(4, 20))