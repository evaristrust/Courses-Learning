# meals = ["Meat", "Rice", "Vegetables", "Tomato", "Ibiraha"]
# # using continue will skip vegetables and move on to other items
# for item in meals:
#     if item == "Vegetables":
#         continue
#     print("I will be able to take {}".format(item))

# meals = ["Meat", "Rice", "Vegetables", "Tomato", "Ibiraha"]
#
# # let's use break to break the loop!
# # before reaching to vegetables, it will stop by their
# for item in meals:
#     if item == "Vegetables":
#         break
#     print("I will be able to take {}".format(item))

# for example, you are going to buy different types of beers except primus
# the seller says everything including primus but you don't wanna it
# do that coding

drinks = ["mtzing", "skol", "panache", "primus"]

let_me_drink = ""

for item in drinks:
    if item == "primus":
        let_me_drink = item
        break
else:
    print("Give me all of those")

if let_me_drink == "primus":
    print("Can I have everything without primus please?")