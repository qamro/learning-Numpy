import numpy as np 

# Matrixes and vectors
A = np.array([[1, 2],
            [3, 4]])
B = np.array([[5, 6],
            [7, 8]])
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])


# calculate Array/Vector/matrix magnitude for all elements in the array
# using this law : sqrt(x² + y² + z² + ....)
print(np.linalg.norm(A))
# calculate the determinant of a matrix
print(np.linalg.det(A))
# calculate the inverse of a matrix
print(np.linalg.inv(A))
# calculate the matrix power any number
print(np.linalg.matrix_power(A, 2)) # here for example we calculate A²
# calculate the rank of a matrix (Number of linearly independent rows/columns)
print(np.linalg.matrix_rank(A))
# Returns only eigenvalues
print(np.linalg.eigvals(A))
# Eigenvalues + Eigenvectors
values, vectors = np.linalg.eig(A)
print(values, vectors)
# Singular Value Decomposition (SVD)
U, S, VT = np.linalg.svd(A)
print(U, S, VT)
# QR Decomposition
Q, R = np.linalg.qr(A)
print(Q, R)
# Matrix Transpose
print(np.transpose(A))
# Matrix Trace (Sum of diagonal elements.)
print(np.trace(A))
# Matrix Multiplication
print(np.matmul(A, B))
# Tensor Product (Kronecker Product) of matrixes
print(np.kron(A, B))
# Dot Product of vectors
print(np.dot(v1, v2))
# Vector Cross Product
print(np.cross(v1, v2))


# solving linear systems 
# suppose u have this linear system
# 2x + 1y = 5
# 1x + 3y = 6
# to solve it we consider a matrix and a vector as its shown
A = np.array([
    [2, 1],
    [1, 3]])
b = np.array([5, 6])

# the two solution x and y are in the variable s
S = np.linalg.solve(A, b)
print(S) # it prints [1.8 1.4] so : x = 1.8 and y = 1.4