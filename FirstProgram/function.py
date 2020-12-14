def my_function(str1, str2):
    print(str1)
    print(str2)


my_function("This is the first one", "This is the second one")
my_function("The Third", "The four")


# Going to deal with another function here and pass arguments

def print_something(name, age, city):
    print("My name is", name, ", and I am", age, "I live in", city)


print_something("Leo Messi", 32, "Barcelona")


# How do we use default arguments?

def find_details(name="someone", age="Unknown"):
    print("My name is", name, "my age is", age)


find_details("Zidane")


# Can we talk about the key arguments?
def find_details(name="someone", age="Unknown"):
    print("My name is", name, "my age is", age)


find_details(age=32)


# Let's now dive deep into passing infinite or flexible arguments into a function

def find_people(*people):
    for person in people:
        print("This person is known as:", person)


find_people("Hesus", "Eugene", "Evajyuno", "Sammy buzzy", "Josephine")


# Next we go learn Return

def do_math(a, b):
    return a + b


math1 = do_math(14, 35)
math2 = do_math(13, 22)

print("The first sum is ", math1, "and the second sum is", math2)

# Learn if, elif, and else

"""Let's say a the 1st student will get a scholarship, the second will get partial, The third Tuition fee,

and the rest will pay"""

class_rank = "Fourth"

if class_rank == "First":
    print("The student will get a Full-Scholarship")
elif class_rank == "Second":
    print("The student will get a Partial-Scholarship")
elif class_rank == "Third":
    print("The student will get a tuition free")
else:
    print("A Student will have to pay the full cost of study")

# Learn a for loop

food = ["Rice", "Potatoes", "Beans", "Cassava", "Irish"]

for items in food:
    print("This item is called ", items)

# Learn the basic of while loop

# Let's say we are going to run numbers
"""
run = True

numbers = 1
while run:
    if numbers == 100:
        run = False
    else:
        print(numbers)
        numbers += 1 """


run = True

print_list = 20

while run:
    if print_list == 200:
        run = False
    else:
        print(print_list)
        print_list += 2
