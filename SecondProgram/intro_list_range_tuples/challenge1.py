# make a program that searches for meals below
# if found the meal without rice,print out the individual items of the meal

menu = []
menu.append(["Sausage", "juice", "banana"])
menu.append(["beans", "tomatoes", "mandazi", "rice"])
menu.append(["beans", "water", "fanta"])
menu.append(["beans", "rice", "fanta", "potatoes"])

# for meal in menu:
#     if not "rice" in meal:
#         print(meal)
#         for items in meal:
#             print(items)

for items in menu:
    if not "rice" in items:
        for value in items:
            print(value)

# Learn how to remove duplicates in a list

my_colors = ["black", "white", "red","yellow", "purple", "white",
             "black", "white","black", "orange", "purple"]

# convert it back to the dictionaries and then back to the list using fromkeys builtin function

remove_duplicates = list(dict.fromkeys(my_colors))

print("The list without duplicates is {}".format(remove_duplicates))

# doing this using function

def my_list(x):
    return list(dict.fromkeys(x))

original_list = ["pens", "books", "books", "notebook", "pens", "notebook"]

print("Your child will need {}: ".format(my_list(original_list)))
