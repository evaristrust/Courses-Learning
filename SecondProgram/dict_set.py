# we are going to learn dictionary and sets
champions = {"epl": "Arsenal, Chelsea, Man utd",
             "laliga": "Barcelona, Real Madrid, Atletico",
             "serie_a": "Juventus, Inter, Ac Milan"}
print(champions)
print(champions["epl"]) # we access the content by not using index, we use keys

champions["ligue1"] = "PSG, Marseille, Lille"
champions["epl"] = "Manchester city, Liverpool, chelsea"
champions["bundesliga"] = "Bayern, Dortmund, Frankfurt"
print(champions)

# what if I want to delete an item from the dict
# Let's delete serie_a
# del champions["serie_a"]
# print(champions)
# deleting an entire dict

# del champions
# print(champions)

# deleting a dict but stay with an empty one so that
# you can input other elements later

# champions.clear()
# print(champions)

# Let's ask a user to put check the top three teams in this championships

# print("Type epl, ligue1, laliga, or serie_a to check the top"
#       "teams in the chosen ligue\nType 'quit' to exit")
#
# while True:
#     check_teams = input("Please Enter a name of a ligue: ")
#     if check_teams == "quit":
#         break
#     description = champions.get(check_teams)
#     print(description)
# you can easily see that if the check_teams is wrong, they print none
# but you can put the condition too as below:

print("Type epl, ligue1, laliga, or serie_a to check the top"
      "teams in the chosen ligue\nType 'quit' to exit")

while True:
    check_teams = input("Please Enter a name of a ligue: ")
    if check_teams == "quit":
        break
    if check_teams in champions:
        description = champions.get(check_teams)
        print(description)
    else:
        print("We don't have {}".format(check_teams))
