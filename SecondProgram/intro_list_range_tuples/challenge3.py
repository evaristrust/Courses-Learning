# Given the tuple below that represents the Imelda May album
# "More Maythem", Write a code to print the album details, followed by a
# listing of all the tracks in the album.
# Indent the tracks by a single tab stop when printing them
# remember that you can pass more than one item to the print function
# separated with a comma

imelda = "More Maythtem", "Imelda May", 2011, \
         ((1, "Pulling the Rug"), (2, "Maythem"), (3, "Pscho"), (4, "Kentish Town waltz"))

name, artist, year, tracks = imelda

print(name)
print(artist)
print(year)
# print("\t",t1, "\t", t2, "\t", t3, "\t", t4)
# the above can work, but also I am going to use for loop
for song in tracks:
    number, title = song
    print("\t the track no. {} is {}".format(number, title))
    # print("\t",song)

# Then the challenge is done and it's done well'

# if you want to buy other tracks on the album for example,
# you would never be able cos the tuple can't be changed
# however, we can store a list in a tuple and the elements of the list only can change

imelda = "More Maythtem", "Imelda May", 2011, \
         [(1, "Pulling the Rug"), (2, "Maythem"), (3, "Pscho"), (4, "Kentish Town waltz")]

imelda[3].append((5, "Halleluya"))
name, artist, year, tracks = imelda
tracks.append((6, "Dance dance"))
print(name)
print(artist)
print(year)
# print("\t",t1, "\t", t2, "\t", t3, "\t", t4)
# the above can work, but also I am going to use for loop
for song in tracks:
    number, title = song
    print("\t the track no. {} is {}".format(number, title))