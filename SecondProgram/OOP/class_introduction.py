# Encapsulation: Do less codes to perform a task
# we are going to create Telephone classes, their origin, models, and price
# Samsung : Korea, sumsung s8 plus, $600
# Samsung : Korea, sumsung s9 plus, $800
# tecno: South Africa, tecno camon cx, $ 200
# iphone: USA, iphone XPro, $1000

class telephones(object):

    def __init__(self, country, model, price):
        self.country = country
        self.model = model
        self.price = price

# create the instances

samsung_s8 = telephones("Korea", "Samsung S8 Plus", 600)
print(samsung_s8.country)
print(samsung_s8.model)
print(samsung_s8.price)

samsung_s9= telephones("Korea", "Samsung S9", 800)
print(samsung_s9.country)
print(samsung_s9.model)
print(samsung_s9.price)

iphone= telephones("USA", "Iphone Xpro", 1000)
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

# that's how we deal with classes

"""
Class: Template for creating objects. All objects created using the same class will have the same characteristics
Object: an instance of a class
Instantiate: Create an instance of a class 
Method: a function defined in a class 
Attribute: a variable bound to an instance of a class 
"""
