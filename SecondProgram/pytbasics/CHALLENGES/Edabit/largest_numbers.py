#print the largest numbers in  a list... n numbers
lst = [20, 42, 21, 34, 23, 70]
lst.sort()
print(lst[-3:]) # print three largest numbers

# or

my_list = [20, 42, 21, 34, 23, 70, 24]
lst = sorted(my_list)
print(lst[-3:])

def largest_numbers(n, lst):
    lst = [20, 42, 21, 34, 23, 70, 24,45]
    my_list = sorted(lst)
    return my_list[len(lst)-n:] # this also works better
print(largest_numbers(5, my_list))

def find_largest(x):
    lst = [45, 20, 21, 89, 45, 65, 100]
    sorted_list = sorted(lst)
    return sorted_list[len(lst)-x:]

print("The top scores in your class are {0}".format(find_largest(3)))

# use this method:
# create a variable outside the function
# works better than the above
my_list = [34, 23, 21, 64, 23, 63, 75, 45] # this looks ugly
def my_largest(x):
    lst = sorted(my_list)
    return lst[len(lst)-x:]

print(my_largest(3))




