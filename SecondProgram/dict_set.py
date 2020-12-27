# # we are going to learn dictionary and sets
# champions = {"epl": "Arsenal, Chelsea, Man utd",
#              "laliga": "Barcelona, Real Madrid, Atletico",
#              "serie_a": "Juventus, Inter, Ac Milan"}
# print(champions)
# print(champions["epl"]) # we access the content by not using index, we use keys
#
# champions["ligue1"] = "PSG, Marseille, Lille"
# champions["epl"] = "Manchester city, Liverpool, chelsea"
# champions["bundesliga"] = "Bayern, Dortmund, Frankfurt"
# print(champions)
#
# # what if I want to delete an item from the dict
# # Let's delete serie_a
# # del champions["serie_a"]
# # print(champions)
# # deleting an entire dict
#
# # del champions
# # print(champions)
#
# # deleting a dict but stay with an empty one so that
# # you can input other elements later
#
# # champions.clear()
# # print(champions)
#
# # Let's ask a user to put check the top three teams in this championships
#
# # print("Type epl, ligue1, laliga, or serie_a to check the top"
# #       "teams in the chosen ligue\nType 'quit' to exit")
# #
# # while True:
# #     check_teams = input("Please Enter a name of a ligue: ")
# #     if check_teams == "quit":
# #         break
# #     description = champions.get(check_teams)
# #     print(description)
# # you can easily see that if the check_teams is wrong, they print none
# # but you can put the condition too as below:
#
# print("Type epl, ligue1, laliga, or serie_a to check the top"
#       "teams in the chosen ligue\nType 'quit' to exit")
#
# while True:
#     check_teams = input("Please Enter a name of a ligue: ")
#     if check_teams == "quit":
#         break
#     if check_teams in champions:
#         description = champions.get(check_teams)
#         print(description)
#     else:
#         print("We don't have {}".format(check_teams))

# see something here too

regions = {"Kigali city": "Gasabo, Kicukiro, Nyarugenge",
             "South": "Nyaruguru, Gisagara, Huye",
             "Noth": "Rulindo, Musanze, Gicumbi",
             "East": "Kayonza, Rwamagana, Ngoma",
             "West": "Rusizi, Nyamasheke, Karongi"}

# for i in range(10):
#     for provinces in regions:
#         print("{} contains: {}".format(provinces, regions[provinces]))
#
#     print("--" * 40)

# let's say we are going to printout sorted keys
# we are going to create a list from the dictionary

# order_regions = list(regions.keys())
# order_regions.sort()

order_regions = sorted(list(regions.keys()))
for x in order_regions:
    print("{}-- {}".format(x,regions[x]))

# what if I want to turn the values of a dict

for f in regions.values():
    print(f)
# use a second method

print("-" * 40)

for key in regions:
    print(regions[key])
# the above method is far more efficient

# then i want to convert the dict_ into a tuple

my_tuple = regions.items()
f_tuple = tuple(my_tuple)
print(f_tuple)

for content in f_tuple:
    province, districts = content
    print("{} contains {}".format(province, districts))

# what if i want to turn my tuple back to dictionary @ i will use dict method

print(dict(f_tuple))