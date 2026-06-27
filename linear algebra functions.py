import numpy as np 

A = np.array([[1, 2],
            [3, 4]])
# calculate Array/Vector/matrix magnitude for all elements in the array
# using this law : sqrt(x² + y² + z² + ....)
print(np.linalg.norm(A))
# calculate Array/Vector/matrix magnitude for all elements in each column
print(np.linalg.norm(A, axis=0))
# calculate Array/Vector/matrix magnitude for all elements in each row
print(np.linalg.norm(A, axis=1))