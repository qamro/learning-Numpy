import numpy as np  

# rng is random numbers generator
rng = np.random.default_rng()
# generate random integers in any range we want
# for example generate random integer between 1 and 100
# the reason why i put high=101 not high= 100 in the range that's the high part in the range is exclusive
print(rng.integers(low=1, high=101)) 
print()
# if we want to generate many numbers in a specific range we just add size part
# and the numbers will be put in 1 dimensional array
print(rng.integers(low=1, high=101, size=3)) # 3 numbers
print(rng.integers(low=1, high=101, size=3)) # 4 numbers
print(rng.integers(low=1, high=101, size=3)) # 6 numbers
print()
# if we want to put all these number in array with dimension we just need to modify size part
print(rng.integers(low=1, high=101, size=(3, 2))) # generate random numbers in 2D array with 3 rows and 2 columns
print(rng.integers(low=1, high=101, size=(4, 5))) # generate random numbers in 2D array with 4 rows and 5 columns
print(rng.integers(low=1, high=101, size=(2, 2))) # generate random numbers in 2D array with 2 rows and 2 columns
print(rng.integers(low=1, high=101, size=(2, 4))) # generate random numbers in 2D array with 2 rows and 4 columns
print(rng.integers(low=1, high=101, size=(3, 2, 2))) # generate random numbers in 3D array with 3 rows and 2 columns and 2 depth
print()

# NOTE:if you want to generate the same random integers forever 
# you just need to add something called a seed and here is its syntax :
# rng = np.random.default_rng(seed=1)
# if you put seed=1 it will generate the same random numbers forever when you run the code again and again and again

# to generate a float number between 0 and 1
print(np.random.uniform())
print()
# to generate a float number in a specific range
print(np.random.uniform(low=0, high=5)) # random float number between 0 and 5
print(np.random.uniform(low=-3, high=5)) # random float number between -3 and 5
print(np.random.uniform(low=-1, high=1)) # random float number between -1 and 1
print(np.random.uniform(low=10, high=20)) # random float number between 10 and 20
print(np.random.uniform(low=-10, high=-5)) # random float number between -10 and -5
print()
# to generate many float number in a specific range we need just to add size
# and the numbers will be put in 1 dimensional array
print(np.random.uniform(low=0, high=5, size=2)) # 2 random float number between 0 and 5
print(np.random.uniform(low=-3, high=5, size=3)) # 3 random float number between -3 and 5
print()
# if we want to put all these number in array with dimension we just need to modify size part
print(np.random.uniform(low=0, high=5, size=(2, 3))) # random float numbers between 0 and 5 in 2D array with 2 rows and 3 columns
print(np.random.uniform(low=-3, high=5, size=(2, 3, 2))) # random float numbers between 0 and 5 in 3D array with 2 rows and 3 columns and 2 depth
print()

# to shuffle and resort an array randomly 
rng = np.random.default_rng()
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)
print()

# to choose a random element in an array
rng = np.random.default_rng()
fruits = np.array(["apple", "strawberry", "banana", "orange", "kiwi", "cherry", "melon"])
fruit = rng.choice(fruits)
print(fruit)
print()
