import numpy as np

mylist = [1,2,3,4]

np.array(mylist)

mylist

type(mylist)

arr = np.array(mylist)

type(arr)

arr

a = np.arange(0,10)

a = np.arange(0,10,2)

np.zeros((5,5))
# np.zeros((row, column))

np.ones((4,4))

type(np.ones((4,4)))

# Random

np.random.randint(0,100)

np.random.randint(0,100, (5,5))

np.linspace(0,10,6)
np.linspace(0,10,101)
np.linspace(0,10,200)

# same random number
# random seed

np.random.seed(101)
np.random.randint(0,100,10)

# operation
arr = np.random.randint(0,100,10)
arr.max()
arr.min()
arr.mean()
arr.argmin()
arr.argmax()

# reshape

arr.reshape(2,5)

# indexing & Masking
mat = np.arange(0,100).reshape(10,10)

mat[9,1]

# get column
mat[:,2]

# get row
mat[2,:]

# operation
mat > 50
mat[mat>50]