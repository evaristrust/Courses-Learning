import numpy as np

arr = np.arange(5)
np.save('myarray', arr)

#Access the saved array
print(np.load('myarray.npy'))

#save and loading multiple arrays
arr1 = np.arange(6)
arr2 = np.arange(7)
arr3 = np.arange(8)

np.savez('saved.npz', x=arr1, y=arr2, z=arr3)
loaded = np.load('saved.npz')
print(loaded['x'])
print(loaded['y'])
print(loaded['z'])

#save an array as a text

identity = np.eye(5)
np.savetxt('myidentity.txt', identity, delimiter=',')
loaded = np.loadtxt('myidentity.txt', delimiter=',')
print(loaded)