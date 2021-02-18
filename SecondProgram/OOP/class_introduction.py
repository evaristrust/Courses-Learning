# Encapsulation: Do less codes to perform a task
# we are going to create Telephone classes, their origin, models, and price
# Samsung : Korea, sumsung s8 plus, $600
# Samsung : Korea, sumsung s9 plus, $800
# tecno: South Africa, tecno camon cx, $ 200
# iphone: USA, iphone XPro, $1000

class Telephones(object):

    selected_phones = "Phones that are on top!"
    # Initializing the class
    def __init__(self, country, model, price):
        self.country = country
        self.model = model
        self.price = price

# create the instances

samsung_s8 = Telephones("Korea", "Samsung S8 Plus", 600)
print(samsung_s8.country)
print(samsung_s8.model)
print(samsung_s8.price)

samsung_s9= Telephones("Korea", "Samsung S9", 800)
print(samsung_s9.country)
print(samsung_s9.model)
print(samsung_s9.price)

iphone= Telephones("USA", "Iphone Xpro", 1000)
print(iphone.country)
print(iphone.model)
print(iphone.price)

print("models: {0}: {1}--${2}, {3}: {4}--${5}"
      "".format(samsung_s8.model, samsung_s8.country,
        samsung_s8.price, iphone.model, iphone.country,
        iphone.price))

print("models: {0.model}: {0.country}--${0.price}, {1.model}: {1.country}--${1.price},"
      "{2.model}: {2.country}--${2.price}"
      "".format(samsung_s8, samsung_s9, iphone)) # simplifying things
# switch the class attributes
print("switch selected phones to BigBrands")
Telephones.selected_phones = "BigBrands"

print(samsung_s8.selected_phones) # show how the instances of a class share the same class attribute
print(samsung_s9.selected_phones)
print(iphone.selected_phones)
print(Telephones.__dict__)
print(samsung_s8.__dict__)




# that's how we deal with classes

"""
Class: Template for creating objects. All objects created using the same class will have the same characteristics
Object: an instance of a class
Instantiate: Create an instance of a class 
Method: a function defined in a class 
Attribute: a variable bound to an instance of a class 
"""
print("......" * 10)
class Epl(object):

    def __init__(self, team, position):
        self.team = team
        self.position = position

one = Epl("ManU", 1)
two = Epl("Liverpool", 2)
three = Epl("Arsenal", 3)

print("The top three teams are: {0.position}. {0.team}\t"
      "{1.position}. {1.team}\t {2.position}. {2.team}".format(one, two, three))
#let's now add two numbers using a class 
class Addition:
    first_number = 0
    second_number = 0
    my_answer = 0

    def __init__(self, f, s):                                    # these are constructors
        self.first_number = f
        self.second_number = s

    def display(self):
        print('The first number is {}'.format(self.first_number))
        print('The second number is {}'.format(self.second_number))
        print('The addition of these numbers is {}'.format(self.answer))

    def my_addition(self):
        self.answer = self.first_number + self.second_number

sum = Addition(1000, 3000)
sum.my_addition()
sum.display()

# learn about a destructor in python  del

class Employee:
    branch1 = []
    branch2 = []
    branch3 = []
    
    def __init__(self, l1, l2, l3):
        self.branch1 = l1
        self.branch2 = l2
        self.branch3 = l3

    def get_staff(self):
        print('The names of staff employees are {}'.format(self.overall))

    def overall(self):
        self.overall = self.branch1 + self.branch2 + self.branch3
    #deleting (calling a destruction)

    def __del__(self):
        print('Destructor called, Employee Class is deleted')

obj = Employee(['Evariste', 'Japhet', 'Venuste'], ['Damour', 'Jado', 'Claude'], ['Octave', 'Ben', 'Francine'])
obj.overall()
obj.get_staff()

del obj




    












