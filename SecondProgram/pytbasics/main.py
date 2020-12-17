# greeting = "Hello"
# str = input("Input your name")
# print(greeting)

str1 = "Your name shows that you are:\n 1. From Rwanda\n 2. Southern Province\n 3. 24 years old"
print(str1)
# above is how we use \n and how we can generate input
# down we are going to see how to use tab
print("1\t2\t3\t4\t5\t6")

# we can also use tripple quotes to write a long string without an issue

str_one = ''' I would like to let you know that
this time i am not going to forgive anybody else.
Thus, you gotta be so serious with your tasks
'''
print(str_one)

# another example using triple quotes

str_two = """He said: "I won't be able to show up! cos i can't do it" \n"""
print(str_two)

# let's perform math

a = 6
b = 9

c = a + b
d = c - a
e = d * b

print("The product is\n", e * 2)

# operators

word = "Hello world"
# skipping... finding an item between 0-6 but skip two items
print(word[0:6:2])

number = "2,2,3,4,3,45,4,5,3,53,5"
print(number[0:6])
# will have to understand this too
print(number[1::3])

Today = "Thursday"

print("hur" in Today) # will return true

print("Day" in Today) # will return false

age = 24

print("I will be {0} years" .format(age))

days = [28, 30, 31]

print("There are " + str(days[0]) + " days in Feb")

#  can do like this too: so amazing using string formatting operation

dates = """
        Jan : {2}
        Feb : {0}
        Mar : {2}
        Apr : {1}
        May : {2}
        June : {1}
        July : {2}
        August : {2}
        September: {1}
        October : {2}
        November : {1}
        December : {2}
        """
print(dates.format(28,30,31))


# Find the square and cubes of numbers from 1 to 12

for i in range(1, 12):
    print("The square of {} is {}\nThe cube is {}".format(i, i**2, i**3))
