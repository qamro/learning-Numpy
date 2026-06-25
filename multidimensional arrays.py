import numpy as np 

# this is 0 dimensional array 
# 0 dimensional array means we pass just any value in our array not a list or a tuple ...etc
array = np.array('A')
print(array.ndim) # we use ndim method to know the number of dimensional of an array
array = np.array()
print(array.ndim)