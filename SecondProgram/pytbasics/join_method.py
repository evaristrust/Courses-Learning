# For example you can print a list like this:
# we are using join method

my_list = ["a", "b", "c", "d"]
f_list = " , ".join(my_list)
print(f_list)

# we are going to perform an exercises of exits...

# We are the following exits:"
# exit 0: You are standing outside of the building, known as exit Q
# exit 1: You are heading to the best supermarket, known as  exit W
# exit 2: You are heading to the ShineBest Bar, known as exit N
# exit 3: You are headed to the Hotel of the city, known as exit S
# exit 4: You will reach to the lake of the city, known as exit E

# We are going to create a dictionary, called locations
# we also have to create a list containing dictionaries of exits: called exits

#creating a dictionaries for locations for each exit
locations = {0: "You are standing outside of the building",
             1: "You are heading to the best supermarket",
             2: "You are heading to the ShineBest Bar",
             3: "You are headed to the Hotel of the city",
             4: "You will reach to the lake of the city"}
# creating a list for exits, putting dictionaries inside
exits = [{"Q": 0},
         {"W": 1, "E": 4, "S": 3, "N": 2, "Q": 0},
         {"N": 2, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 2, "W": 1, "Q": 0},
         {"W": 1, "S": 3, "Q": 0}]

# initializing loc

loc = 1

while True:
# Accessing the available exits in the exit list and printing the matching locations
    available_exits = " , ".join(exits[loc].keys())
 # if the loc is 0, we are going to break the loop
    if loc == 0:
        break
    direction = input("choose from these available exits: {} ".format(available_exits)).upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("Sorry! We are unable to find that location")








