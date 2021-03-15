# Find the second largest number in a list
# Just in a simple way.,. like a beginner
def second_max():
    # n = [3, 53, 53, 23, 40, 45]
    print('Find the second largest number in a given list of your numbers')
    n = [int(n) for n in input("Enter multiple value: ").split(',')]
    # change it to set to remove duplicates
    my_set = set(n)
    # Bring back a new list from set
    my_list = list(my_set)
    my_list.sort()
    return my_list[-2]

print(second_max())
