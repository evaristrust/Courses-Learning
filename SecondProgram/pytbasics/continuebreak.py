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
#
drinks = ["mtzing", "skol", "panache", "amstel", "primus" ]

let_me_drink = ""

for item in drinks:
    if item == "primus": # when you find primus, stop
        let_me_drink = item
        break
else:
    print("Give me all of those")

if let_me_drink == "primus":
    print("Can I have everything without primus please?")

#
# watch_games = ["Football","Basket", "Box","Tennis" , "Volleyball"]
#
# funny_game = ""
#
# for item in watch_games:
#     if item == "Box":
#         funny_game = item
#         break
# else:
#     print("I will watch all of these games")
#
# if funny_game == "Box":
#     print("Can I have tickets for all other games excluding Box?")


# in the list of destinations, choose your destinations without Rusizi

destinations = ["Kigali", "Rusizi","Butare", "Musanze", "Rwamagana"]

let_me_go = ""

for place in destinations:
    if place == "Rusizi":
        let_me_go = place
        break
    else:
        print("I will go to those places")

if let_me_go == "Rusizi":
    print("Can I go to other places without {}".format(let_me_go))



# types of churches in rwanda

churches = ['Catholics', 'Islam', 'protestant', 'Adventist']

# we want to select a girlfriend from any church except islam or adventists
choose_girl = ''
for girl in churches:
    if girl == 'islam' or girl == 'adventist':
        choose_girl = girl
        print('Can i get a pass of any girl except islams and adventists? Thanks!')
        break
else:
    print('She can be my girlfriend')




