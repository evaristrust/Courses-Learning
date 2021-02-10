# # Example 1
# odd = [1, 3, 5, 7, 9]
#
# even = [2, 4, 6, 8]
#
# numbers = odd + even
# # numbers.sort()
# sorted_numbers = sorted(numbers)
#
# if sorted_numbers == numbers:
#     print("They are equal")
# print("They are not equal")
#
# print(sorted_numbers)
#
# # Example 2
# beers = ["laga", "primus", "petit skol", "knowless"]
# beers.append("heinken")
# for alcohol in beers:
#     print("This is: ", alcohol)

# example 3.
#
# even_numbers = [2, 4, 6, 8]
# sorted_even = even_numbers
# even_numbers.sort(reverse=True)
# print(even_numbers)
#
# ## N.B
#
# print(even_numbers is sorted_even)
#
# # but
# even_numbers = [2, 4, 6, 8]
# sorted_even = list(even_numbers)
#
# print(sorted_even is even_numbers)
# this will print false because sorted_even is a new list

# but again

# print(sorted_even == even_numbers)
# this will return true because the content of the list is the same and in the same order

# but
# sorted_even = sorted(even_numbers, reverse=True)
# print(sorted_even == even_numbers)
# # this will print false! just because the order is not the same
#
odd_num = [1, 3, 5, 7]
even_num = [2, 4, 6, 8]

get_numbers = [odd_num, even_num]

print(get_numbers)

for items in get_numbers:
    print(items)
    for value in items:
        print(value)

# Another example:
menu = []
menu.append(["Sausage", "juice", "banana"])
menu.append(["beans", "tomatoes", "mandazi", "rice"])
menu.append(["beans", "water", "fanta"])
menu.append(["beans", "rice", "fanta", "potatoes"])

for items in menu:
    if not "rice" in items:
        print(items)

