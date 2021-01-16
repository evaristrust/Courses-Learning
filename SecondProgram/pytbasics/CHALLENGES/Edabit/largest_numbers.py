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
    return my_list[len(lst)-n:] # this also works
print(largest_numbers(4, my_list))