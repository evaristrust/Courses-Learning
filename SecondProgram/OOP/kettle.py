class kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False
    def swith_on(self):
        self.on = True

hamilton_kettle = kettle("Hamilton", 12)
kenwood_kettle = kettle("Kenwood", 15)

print("Models: {0.make} = ${0.price}, {1.make} = ${1.price}"
      "".format(hamilton_kettle,kenwood_kettle))

print(hamilton_kettle.on) # False
hamilton_kettle.swith_on()
print(hamilton_kettle.on) # True
kettle.swith_on(kenwood_kettle )
print(kenwood_kettle.on) # Returns true
kenwood_kettle.swith_on()

print("*" * 80)
kenwood_kettle.power = 1.5
print(kenwood_kettle.power)