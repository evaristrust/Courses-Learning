import numpy as np
import webbrowser

arr2k = np.arange(15)
arr_sqrt = np.sqrt(arr2k)
print('SQUARE ROOT:')
print(arr_sqrt)
print('SQUARE:')
print(np.square(arr2k))
print('EXPONENTIAL, e to the power of elements:')
print(np.exp(arr2k))

#1. generate two random arrays using built methods and add these two arrays

arr1 = np.random.randn(10) #randn: random distribution
arr2 = np.random.randn(10)
print('\nRANDOM ARRAYS:')
print(arr1)
print(arr2)
#ADD THEM
print('\nADDTION:')
arr12 = np.add(arr1, arr2)
print(arr12)
#COMPARE THE MAXIMUM VALUES IN BOTH ARRAYS
print('\nMAXIMUM:')
print(np.maximum(arr1, arr2)) #COMPARE VALUES IN BOTH ARRAYS AND RETURN MAX AT EACH VALUE

#for universal functions: open this link
# website = 'https://numpy.org/doc/stable/reference/ufuncs.html'
# webbrowser.open(website)

