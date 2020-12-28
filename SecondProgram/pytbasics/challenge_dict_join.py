
# Modify the program in the join file so that
# so that the exits is a dictionary rather than a list
# with the keys being the numbers of the locations and the values
# being dictionaries holding the exits (as they do at present).
# No change should be needed to the actual code
#
# once that is working, create a nother dictionary that contains words
# that players may use. These words will be the keys, and thteir
# values will be a single letter that the program can use to
# determine which way to go

#creating a dictionaries for locations for each exit
locations = {0: "You are standing outside of the building",
             1: "You are heading to the best supermarket",
             2: "You are heading to the ShineBest Bar",
             3: "You are headed to the Hotel of the city",
             4: "You will reach to the lake of the city"}
# creating a list for exits, putting dictionaries inside
exits = {0: {"Q": 0},
         1: {"W": 1, "E": 4, "S": 3, "N": 2, "Q": 0},
         2: {"N": 2, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 2, "W": 1, "Q": 0},
         5: {"W": 1, "S": 3, "Q": 0}}

# creating a dictionary of vocabularies or words that the player can use

vocabs = {"NORTH": "N",
          "SOUTH": "S",
          "WEST": "W",
          "EAST": "E",
          "QUIT": "Q"}

# initializi5g loc

loc = 1

while True:
# Accessing the available exits in the exit list and printing the matching locations
    available_exits = " , ".join(exits[loc].keys())
    print(locations[loc])
 # if the loc is 0, we are going to break the loop
    if loc == 0:
        break
    direction = input("choose from these available exits: {} ".format(available_exits)).upper()
    print()

    #parse the user input, using our vocabs dictionary
    if len(direction) > 1: # if it is more than one letter
        for word in vocabs: # check all the words that are in the vocabs
            if word in direction: # did the user put the word we know?
                direction = vocabs[word]
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("Sorry! We are unable to find that location")
