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

#5. Get out some elements of colums
arr2d = np.array([[10, 20, 40], [30, 60, 120], [40, 70, 130]])
print(arr2d)
print(arr2d[:2,1:]) #getting 2d array from the parent array starting on position 1

"""
---create a zeros array of 10 by 10
--- use a for loop to change the elements 
"""

arr1_zero = np.zeros([10, 10])
#check the length of the array
arr1_zero_length = arr1_zero.shape[1]

#for loop

for i in range(arr1_zero_length):
    # arr1_zero[i] = 2
    arr1_zero[i] = i
print(arr1_zero)

# fancy indexing
print(arr1_zero[[2, 4, 6, 8]])

#6. working with 3d matrix
print('3D MATRIX:')
my3d = np.arange(50).reshape(5,5,2)
print(my3d)
print('3D MATRIX TRANSPOSE:')
my3d_transpose = my3d.transpose(1, 0, 2)
print(my3d_transpose)

#7. Swipping axes:
arr4 = np.array([[1, 4, 3]])
print(arr4.swapaxes(0, 1))


