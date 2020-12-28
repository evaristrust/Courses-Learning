# we gonna discuss about sets
# set are unordered, but are quite similar to dicts but aren't accessible using keys
# they don't use duplicates...each item is counted once
# printing them results into any order
animals = {"dog", "cows", "hen", "fish", "lion", "fish"}
print(animals)

# if we want to add new animals

# animals.add("tiger")
# print(animals)

# you can also use for

for animal in animals:
    print(animal)

# let's say i want to create set of wild animals
# using set function

wild_animals = set(["dog", "lion", "tiger", "zebra"])
print(wild_animals)

# the better way of doing empty set is to use set constructor
# rather than using empty curely braces

empty_set = set()
empty_set.add("erroo")
print(empty_set)

# use range and see

even_numbers = set(range(0, 40, 2))
print(even_numbers)

# turn a tuple into a set

squares = (4, 9, 16,36,25, 49, 64)

square_set = set(squares)
print(square_set)

# let's introduce union and intersections


print(even_numbers.union(square_set))
print(len(even_numbers))
print(len(even_numbers.union(square_set)))
print(len(square_set))
# you will see why we didn't get the length of the union 27
# as 20 + 7 is 27... this is because of the intersections numbers
# and a set components don't even get duplicated

# let's deal with intersections
# two ways... using intersection method or using ampersand

print("--" * 40)
print(even_numbers & square_set)
print(even_numbers.intersection(square_set))
# these are the same results

# let's see how to sort them
print(sorted(square_set))

# how about the difference... like elements in even_numbers that are not in square_set
# same as even_numbers - square_set
print("--" * 40)
print(even_numbers - square_set)
print("even_numbers minus square_set is: ", even_numbers.difference(square_set))

print("--" * 40)

print(even_numbers.difference_update(square_set)) # this return none

even_numbers.difference_update(square_set) # this return the difference
print(even_numbers)

# symetric difference: returns the elements of the union of sets minus the intersection

print("***" * 40)
print(sorted(even_numbers.symmetric_difference(square_set)))
print(sorted(square_set.symmetric_difference(even_numbers)))

# just added sorted to show you that the result is still the same

# let's discusss discard and remove an element from a set
# discard won't throw an error when removing unexisted element
# remove will throw it
print("****" * 40)
print("We are going to see the difference btn discard and remove")
square_set.remove(4)
print(square_set)
square_set.discard(4)
print(square_set)
square_set.discard(8)
print(square_set)
# square_set.remove(8) # this will throw an error
print(square_set)

# using discard is safe
# but in some cases u will need to use remove just to detect an error
# cos discard won't tell u if an element was included

#let's using try and except

try:
    square_set.remove(8)
except KeyError:
    print("4 is not included in the set")

# subsets and supersets :: subsets when all elements are contained in the other set
# superset: it has a subset elements and others
print("//" * 40)
print("we are going to learn subset and supersets")
square = (4,9, 16, 36)
square_numbers = set(square)
even_numberz = set(range(0, 40, 2))
if square_numbers.issubset(even_numberz):
    print("one is a subset of another")
if even_numberz.issuperset(square_numbers):
    print("one is a superset of another!")
else:
    print("They are not subset or supersets")

# frozen set is immutable
# you can do intersections, union, or subtract from another
# but you can't do a symmetric_difference or difference_update

odd = frozenset(range(1, 10, 2))
print(odd)

# challenge.............
# create a  program that takes some text and returns a list of
# all the characters in the text aht are not vowels,
# sorted in alphabetical order
# you can either enter the text from the keyboard
# or inialise a string variable with the string
print("---" * 40)
example = "I will even die an arsenal fan unless you mothefuckers are shouting"

# create a set of vowels

vowels = frozenset("aiueo")
# create a set of example

example_set = set(example)

final_set = example_set.difference(vowels)
print(sorted(final_set))