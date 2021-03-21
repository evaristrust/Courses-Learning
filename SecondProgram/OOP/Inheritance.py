# Inheritance is the capability of one class
# to derive or inherit the properties from another class
# note that there object in brackets... class Person is equiv to Person(Object)
class Person(object):
    #initializing
    def __init__(self, name):
        self.name = name
    #get the name of person
    def get_name(self):
        return self.name
    # check if d person is an employee
    def is_employee(self):
        return False
#creating a subclass.. not Person is in the brackets
class Employee(Person):
  def is_employee(self):
      return True

# code drivers here down

emp = Person('Dev1') #An object of Person
print(emp.get_name(), emp.is_employee())
emp = Employee('Dev2') #An object of Employee
print(emp.get_name(), emp.is_employee())

#going to create a program that shows
# the name of a staff, idnumber, position, and salary

class Individual(object):
    def __init__(self, name, id_number):
        self.name = name
        self.id = id_number

    def display(self):
        print('Details are:\nName: {}\nID: {}\nSalary: '
              '{}\nPosition: {}'.format(self.name, self.id, self.salary, self.position))

#inherited or subclass
class Employee(Individual):
    def __init__(self, name, id_number,position, salary):
        self.position = position
        self.salary = salary
    #invoking the parent class
        Individual.__init__(self, name, id_number)

p = Employee('Sami HeadedBuzzy', 'IE2010230', 3000, 'Intern')
p.display()

#The above is a single inheritance
#N.B: Invoking the __int__ of the parent class is a must
# otherwise, it will throw an error

# We now going to learn the multiple inheritance in py
# ERROR:__init__() takes 4 positional arguments but 8 were given

class Woman(object): # parent class 1
    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level

    def display_result(self):
        print('Details of my frau are: '
              'Name: {}\nAge: {}\nEducation Level: {}\nSchool Attended: {}'
              'Born City: {}\nHeight: {}\nSalary: ${}\nHasAJet: {}'
              .format(self.name, self.age, self.level, self.school, self.city,
                      self.height, self.salary, self.hasjet))

class Girl_f(object): # parent class 2
    def __init__(self, school, city, height):
        self.school = school
        self.city = city
        self.height = height

class Date_her(Woman, Girl_f): # child class of two parents 
    def __init__(self, name, age, level, school, city, height, salary):
        self.salary = salary
        self.hasjet = True
        Girl_f.__init__(self,school, city, height)
        Woman.__init__(self,name, age, level)

w = Date_her('Taylor Swift', 30, 'PhD in Music', 'Havard Music School', 'New York',
          1.79, 400000)
w.display_result()


# Learn Multilevel inheritance: Child and Grandchhild relationship

class Base:
    #constructor
    def __init__(self, name):
        self.n = name
    #getName
    def get_name(self):
        return self.n
#child
class Child(Base):
    def __init__(self, name, age):
        self.age = age
        #Invoking the __init__ of the base class
        Base.__init__(self, name)
    #getAge
    def get_age(self):
        return self.age
#grandChild
class grand_child(Child):
    def __init__(self, name, age, address):
        self.address = address
        #Invoking __init__ for child (parent of grand_child)
        Child.__init__(self, name, age)
    #getAddress
    def get_address(self):
        return self.address

c = grand_child('MyChild', 20, 'KG 08 AV 108, KIGALI VEGAS')
print('My child info:\n{} {} {}'.format(c.get_name(), c.get_age(), c.get_address()))

# Hierarchical inheritance
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class1
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

# Derived class2
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()










