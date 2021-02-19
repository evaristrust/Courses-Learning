#Polymorphism simple means ocurring in many forms
# example: a function can be the same but works on different data types
len('Evariste')
len([1,2,42,342,1])

#example on the function
def add(x, y, z = 0):
    return x - y + z

print(add(4, 2)) # this works
print(add(8, 3, 2)) # this works too

# Polymorphism in class types: Example

class Rwanda(object):
    def capital(self):
        print('Kigali is the capital city of Rwanda')
    def languages(self):
        print('Kinyarwanda is the mother tongue and spoken with everyone')
    def type(self):
        print('Rwanda is a developing country')
    def location(self):
        print('It is located in the EAC')

class Germany(object):
    def capital(self):
        print('Berlin is the capital city of Germany')
    def languages(self):
        print('Deutch/German is the mother tongue and spoken with everyone')
    def type(self):
        print('Germany is a developed country')
    def location(self):
        print('It is located in the EU/Shengeni')


rda = Rwanda()
gmn = Germany()
# create a for loop
for country in (rda, gmn):
    country.capital()
    country.languages()
    country.type()
    country.location()

print('##' * 40)
#Poly with inheritance
class Taylor:
    def album(self):
        print('Reputation is dope')
    def track(self):
        print('Gergeous is a top-notch')

class Swift(Taylor):
    def album(self):
        print('Evermore is dope recent album')
    def track(self):
        print('Champagne problems is a my favorite in the album')

obj1 = Taylor()
obj2 = Swift()
for music in (obj1, obj2):
    music.album()
    music.track()

#Polymorphism with a Function and objects
print('**' * 40)
class USA(object):
    def capital(self):
        print('Washington is the capital city of Rwanda')
    def languages(self):
        print('English is the mother tongue and spoken with everyone')
    def type(self):
        print('USA is a developed country')
    def location(self):
        print('It is located in the North America')

class Italy(object):
    def capital(self):
        print('Roma is the capital city of Germany')
    def languages(self):
        print('Italian is the mother tongue and spoken with everyone')
    def type(self):
        print('Italy is a developed country')
    def location(self):
        print('It is located in the EU/Shengeni')

#Creating a function here to drive codes
def func(obj):
    obj.capital()
    obj.languages()
    obj.type()
    obj.location()

usa_obj = USA()
italy_obj = Italy()

#Invoking the function here:
func(usa_obj)
func(italy_obj)