import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

points = np.arange(-5,5,0.01)
dx, dy = np.meshgrid(points,points)
print(dx)
print(dy)
z = (np.sin(dx) + np.sin(dy))
print(plt.imshow(z)) #ploting our stf
print(plt.colorbar())
print(plt.title('MY FIRST PLOT'))

#List comprehension
A = np.array([1, 2, 4, 8])
B = np.array([100, 200, 400, 800])

condition = np.array([True, True, False, False])
answer = [(A_val if cond else B_val) for A_val, B_val, cond in zip(A, B, condition)]
print(answer)

#much more convenient fashion using numpy where
answer2 = np.where(condition,A,B)
print(answer2)

arr = randn(5,5)
print(arr)
#use condition to set negative values to zero
results = np.where(arr<0, 0, arr)
print(results)

#some stastical concepts or binary operations
C = np.array([[1, 2, 3], [3, 5, 6], [8, 9, 11]])

print(C.sum())
print(C.sum(0))
print(C.sum(1))
print(C.mean()) #mean
print(C.std()) #standard deviation
print(C.var()) #variance

#working with booleans

boolean_1 = np.array([True, False, False])
print(boolean_1.any()) # True if any is True
print(boolean_1.all()) # True if all are True

#working with sort()
original = randn(5)
print(original)
original.sort()
print(original)

#check an array unique, in1d
countries = np.array([
    'Rwanda', 'USA', 'Germany',
    'USA', 'Mexico', 'Austria',
    'Germany', 'Burundi', 'DRC'
])

countries_unique = np.unique(countries)
print(countries_unique)

check_countries = np.in1d(['France', 'Rwanda', 'DRC', 'England'], countries)
print(check_countries) # will check if an item is in the array
















