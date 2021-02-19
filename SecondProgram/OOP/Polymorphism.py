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