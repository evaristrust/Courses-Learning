import numpy as np

#1. creating arrays

my_list = [1, 2, 4, 6, 8]
arr1 = np.array(my_list) # then print this
my_list2 = [3, 5, 7, 9, 11]
my_lists = [my_list, my_list2]
my_arr2 = np.array(my_lists)
print('COMBINED ARRAY:')
print(my_arr2)

#2. checking the shape for the array and dypes
print('COMBINED ARRAY SHAPE AND TYPE:')
print(my_arr2.shape)
print(my_arr2.dtype)

#3. creating zeros and ones array, and identity matrix
my_zeros_array = np.zeros(5)
print('ZEROS:')
print(my_zeros_array) # decimal points there and the dtype throw float64
print(my_zeros_array.dtype)

my_empty_array = np.empty(5)
print('EMPTY ARRAY:')
print(my_empty_array)

my_ones_array = np.ones(5)
print('ONES:')
print(my_ones_array)
print('ONES MATRIX:')
print(np.ones([5,5])) #For matrix printing

print('IDENTITY MATRIX:')
print(np.eye(5))

#4. creating arange...
print('RANGE FROM 5 TO 100 WITH INTERVAL OF 5:')
print(np.arange(5,100, 5))
