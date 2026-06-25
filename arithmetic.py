import numpy as np 

#that's the difference between simple lists and numpy arrays
my_list = [1, 2, 3, 4] 
my_list = my_list * 2   # here it duplicates the list twice
print(my_list)
array = np.array([1, 2, 3, 4])
array = array * 2    # here it does the product by 2 operation for each element in the array
print(array)