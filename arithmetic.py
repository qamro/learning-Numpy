import numpy as np 
# git commit -m "arithmetic operations"
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