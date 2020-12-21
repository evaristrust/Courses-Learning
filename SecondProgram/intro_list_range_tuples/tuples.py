# Tuples are kinda lists but they are ordered set of data
# They are immutable! meaning, they cannot be changed
# attempting to add or append an item to a tuple would throw an error
# mostly put inside a paranthesis but it's not necessary but it's so encouraged to do so
a = "a", "b", "c"
print(a)
print("a", "b", "c")

# but
print(("a", "b", "c"))
# so recommended to use paranthesis
# remember list is a list of items of the same category!
# tuple can contain items from different categories! let's take an example of albums
# name of album, artist, and a year of release

album_one = ("Romance", "Camila", 2019)
album_two = ("El negreto", "Akon", 2019)
album_three = ("Plus", "Ed Sheran", 2011, (1, "party"), (2, "HelloGod"), (3, "Salute"))
print(album_one)
print(album_two)
print(album_three)
print(album_three[2])
# album_one[0] = "Lover" # this will throw an error
# but
album_one = album_one[0], "Camil", album_one[2]
print(album_one)

# if you want to store data that wn't change, use tuple.. else
# use list

# here is another example

name, artist, year, track1, track2, track3 = album_three
print(name)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)




