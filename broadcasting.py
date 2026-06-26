import numpy as np 

# broadcasting allows NumPy to perform operations on arrays
# broadcasting allows arrays of different shapes to be used together in arithmetic operations
# broadcasting performs these operations by virtually expanding dimensions
# so the arrays of different shapes match the larger array's shape
# to broadcast the arrays either:
# the dimensions (row or column or depth) must be the same size for all the arrays
# or one of their dimension is 1
array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])
print(array1.shape)
print(array2.shape)
# since the size of one of the array's rows is 1 and the size of one of the array's columns is 1
# array1 and array2 can be broadcasted
print(array1 * array2)
print(array1 + array2)



# small exercise
# the table of multiplication
array3 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array4 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
print(array3.shape)
print(array4.shape)
# since the size of one of the the array's rows is 1 and the size of one of the the array's columns is 1
# array3 and array4 can be broadcasted
print(array3 * array4)


