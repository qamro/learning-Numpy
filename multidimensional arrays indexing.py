import numpy as np 

# this is 1 dimensional array using a list
array = np.array(['A', 'B', 'C', 'D'])
# to access to an element from this array we use indexing
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print()

# this is 2 dimensional array using a list
array = np.array([['A', 'B', 'C', 'D'], ['Q', 'S', 'F', 'G'], ['H', 'J', 'K', 'L']])
# to access to an element from this array we use indexing
print(array[0, 0])
print(array[1, 3])
print(array[2, 1])
print(array[0, 1])
print()

# this is 3 dimensional array using a list
array = np.array([[['A', 'B', 'C', 'D'], ['Q', 'S', 'F', 'G'], ['H', 'J', 'K', 'L']],
            [['P', 'N', 'V', 'X'], ['W', 'M', '0', '9'], ['4', '3', '2', '1']],
            [['O', 'I', 'U', 'Y'], ['T', 'R', 'E', 'Z'], ['a', 'b', 'c', 'd']]])
# to access to an element from this array we use indexing
print(array[0, 0, 0])
print(array[1, 1, 2])
print(array[2, 1, 0])
print(array[0, 1, 1])
