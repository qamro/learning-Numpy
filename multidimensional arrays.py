import numpy as np 

# this is 0 dimensional array 
# 0 dimensional array means we pass just any value in our array not a list or a tuple ...etc
array = np.array('A')
print(array.ndim) # we use ndim method to know the number of dimensional of an array
# this is 1 dimensional array using a list
array = np.array(['A', 'B', 'C', 'D'])
print(array.ndim)
# this is 0 dimensional array using a tuple
array2 = np.array(('A', 'B', 'C', 'D'))
print(array2.ndim)
# this is 2 dimensional array using a list 2D
array3 = np.array([['A', 'B', 'C', 'D'], ['Q', 'S', 'F', 'G'], ['H', 'J', 'K', 'L']])
print(array3.ndim)
# this is 3 dimensional array using a list 3D
array4 = np.array([[['A', 'B', 'C', 'D'], ['Q', 'S', 'F', 'G'], ['H', 'J', 'K', 'L']],
            [['P', 'N', 'V', 'X'], ['W', 'M', '0', '9'], ['4', '3', '2', '1']],
            [['O', 'I', 'U', 'Y'], ['T', 'R', 'E', 'Z'], ['a', 'b', 'c', 'd']]])
print(array4.ndim)
print(array4.shape) #we use shape method to know (the depth, the number of rows, the number of columns)

