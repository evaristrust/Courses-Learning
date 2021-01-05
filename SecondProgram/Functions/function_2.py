def get_water():
    width = 80
    text = "WASAC is fucking us in the ass"
    left_margin = width - len(text)
    print(" " * left_margin, text)

get_water()

# using for loop in a function

# def new_hits(*args):
#     songs = ""
#     for arg in args:
#         songs += str(arg) + "**" # a separator here
#     print(songs)
# new_hits("Samoya", "Igare", "Micro", "Ubushyuhe")

# modify the codes a bit mn!
# def new_hits(*args, sep= "**", end='\n', file=None, flush=False):
#     songs = ""
#     for arg in args:
#         songs += str(arg) + sep
#     print(songs, end=end, file=file, flush=flush)
# new_hits("Samoya", "Igare", "Micro", "Ubushyuhe")

# sending data into a file, a new file that we are going to open down there!
def new_hits(*args, sep= "**", end='\n', file=None, flush=False):
    songs = ""
    for arg in args:
        songs += str(arg) + sep
    print(songs, end=end, file=file, flush=flush)

with open("songs", mode="w") as songs_file:
    new_hits("Samoya", "Igare", "Micro", "Ubushyuhe", file=songs_file)

# let's try something like return in the function and see what it is!
def new_hits(*args, sep= "**", end='\n', file=None, flush=False):
    songs = ""
    for arg in args:
        songs += str(arg) + sep
    return songs

print(new_hits("Samoya", "Igare", "Micro", "Ubushyuhe"))
