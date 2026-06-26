import numpy as np 

# scalar arithmetic
array = np.array([1, 2, 3])
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)  # ** that means power 
print()

# vectorized math functions
array = np.array([1, 2, 3])
print(np.sqrt(array))
print(array * np.pi)
print(array * np.e)
print((array ** 2) * np.pi)  # calculating area of circle with radius values in the array
array2 = np.array([1.09, 2.34, 3.87])
print(np.round(array2))
print(np.floor(array2))
print(np.ceil(array2))
print()

# arrays arithmetic
array3 = np.array([1, 2, 3])
array4 = np.array([4, 5, 6])
print(array3 + array4)
print(array3 - array4)
print(array3 * array4)
print(array3 / array4)
print(array3 ** array4)
print()

# comparison operators
scores = np.array([10, 15, 7, 20, 19, 3])
# that returns a boolean array
print(scores == 20) 
print(scores >= 10) 
print(scores < 10) 
# we can also use indexing to assign new values to our array elements
# for example
scores[scores < 10] = 0
print(scores)
