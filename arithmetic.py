import numpy as np 

# scalar arithmetic
array = np.array([1, 2, 3])
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)  # ** that means power 

# vectorized math functions
array = np.array([1, 2, 3])
print(np.sqrt(array))
array2 = np.array([1.09, 2.34, 3.87])
print(np.round(array2))
print()