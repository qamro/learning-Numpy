import numpy as np  

# rng is random numbers generator
rng = np.random.default_rng()
# generate random integers in any range we want
# for example generate random integer between 1 and 100
# the reason why i put high=101 not high= 100 in the range that's the high part in the range is exclusive
print(rng.integers(low=1, high=101)) 
# if we want to generate many numbers in a specific range we just add size part
# and the numbers will be put in 1 dimensional array
print(rng.integers(low=1, high=101, size=3)) # 3 numbers
print(rng.integers(low=1, high=101, size=3)) # 4 numbers
print(rng.integers(low=1, high=101, size=3)) # 6 numbers
# if we want to put all these number in array with dimension we just need to modify size part
print(rng.integers(low=1, high=101, size=(3, 2))) # generate random numbers in 2D array with 3 rows and 2 columns
print(rng.integers(low=1, high=101, size=(4, 5))) # generate random numbers in 2D array with 4 rows and 5 columns
print(rng.integers(low=1, high=101, size=(2, 2))) # generate random numbers in 2D array with 2 rows and 2 columns
print(rng.integers(low=1, high=101, size=(2, 4))) # generate random numbers in 2D array with 2 rows and 4 columns
print(rng.integers(low=1, high=101, size=(3, 2, 2))) # generate random numbers in 3D array with 3 rows and 2 columns and 2 depth
