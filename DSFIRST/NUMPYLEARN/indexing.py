import numpy as np

arr1 = np.arange(0, 20, 2)
print(arr1)

#1. Access the number
print(arr1[6])
print(arr1[4:9])

#2. Set the range with other values
arr1[4:9] = 200
print(arr1)

#3. changing all elements in an array
my_new_array = np.arange(0,30,3)
print(my_new_array)

my_new_array_slice = my_new_array[1:6]
print(my_new_array_slice)
my_new_array_slice[:] = 21 #Setting all sliced elements to 21
print(my_new_array_slice)

#4. printing the original array.. it will be modified
print(my_new_array) #The original array just got modified
# use copy method to avoid the original arr modification

other_array = np.arange(2, 12, 2)
other_array_copy = other_array.copy()
other_array_slice = other_array_copy[1:4]
print(other_array_slice)
other_array_slice[:] = 45
print(other_array_slice)
print(other_array)
