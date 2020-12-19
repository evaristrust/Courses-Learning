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