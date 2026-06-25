import numpy as np 

# 2D array
array = np.array([[1, 2, 3, 4],  # index 0
                [5, 6, 7, 8],   
                [9, 10, 11, 12],  
                [13, 14, 15, 16]])   # index 4


# we start with rows slicing
# for slicing our array we do just like we do in the strings
# array[start: end: step]
# the end index in both the arrays and the strings is exclusive 
# the last index in our array for example is 4 when we use him as an end index and it is 3 when we use him as a start index
# this case is only for the end index
print(array[0])
print()  # for space
print(array[::2])   
print()
print(array[::-1])  # the reversed array
print()
print(array[::-2])
print()
print(array[1:4])
print()
print(array[-1])
print()
print(array[3])
print()
print(array[0::3])
print()
print(array[::-3])
print()
print(array[0:4:2])
print()
print()
print()




# column slicing
# if we want to select specific elements in the columns 
# we use this syntax array[row, column]

# we want to slice the first columns with index 0 in all rows
print(array[:, 0])
print() 
# we want to slice the first columns with index 0 in the first and the third rows
print(array[0::2, 0])
print() 
# we want to slice the second columns with index 1 in the last row
print(array[-1, 1])
print() 
# we want to slice the last columns in all rows
print(array[:, -1])
print() 
# we want to slice the last columns with in all rows in reverse order
print(array[::-1, -1])
print() 
# we want to slice the first three columns in all rows
print(array[:, 0:3])
print() 
# we want to slice the last three columns in all rows (we skip the first column)
print(array[:, 1:4])
print() 
# we want to slice the first three columns in the first and the third rows
print(array[0::2, 0:3])
print() 
# we want to slice the first and the third columns in all rows
print(array[:, 0::2])
print()
# we want to slice the first and the third columns in the first row
print(array[0, 0::2])
print()  
# we want to slice the last two columns in all rows
print(array[:, 2:4])
print() 
# we want to slice the columns in reversed order in all rows
print(array[:, ::-1])
print() 
# we want to slice the columns in reversed order in all rows in reversed order also
print(array[::-1, ::-1])
print() 
# we want to slice the second and the last columns in reversed order in all rows
print(array[:, ::-2])
print() 
# we want to slice the first and the second columns in the first and the second rows
print(array[0:2, 0:2])
print() 
# we want to slice the third and the last columns in the first and the second rows
print(array[0:2, 2:])
print() 
# we want to slice the first and the second columns in the third and the last rows
print(array[2:, 0:2])
print() 
# we want to slice the third and the last columns in the third and the last rows
print(array[2:, 2:])
print() 