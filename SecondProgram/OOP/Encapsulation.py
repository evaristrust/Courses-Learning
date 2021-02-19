#Encapsulation: provides protection of your data, no easy access.. nor easy data modification
# Sales data are accessed by sales team except when permission is asked by someone outside

#Encaps uses two methods of data protection : Private members and protected members

#protected members:
#These data cannot be accessed outside of a class but can inside a class or subclass
#The convention is to put an underscore to the object or variable

class A:
    def __init__(self):
        self._a = 10 # protected member

class B(A):
    def __int__(self):
        A.__init__(self)
        print('Calling the protected member of the base class: ')
        print(self._a)

w = B()
c = A()
# print(c.a) # this will throw an error: AttributeError: 'A' object has no attribute 'a'

# Private members: The convention is to put a double underscore to the object

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "Geek1 is getting out of the game"
        self.__b = "Geek2 is getting out of the pitch"

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__b)


# Driver code
obj = Base()
print(obj.a)
# print(obj.b) or print (obj.__b) will throw an error