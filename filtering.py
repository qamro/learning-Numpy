import numpy as np 

ages = np.array([[22, 18, 17, 32, 26, 20, 45, 15],
                [24, 16, 30, 65, 23, 28, 40, 39]])
# now we can class and filter these data 
# when we filter an array according to a condition then we create new array
# this new array it is always 1 dimension
# in python we use and or in numpy we use the logical and |
# in python we use and and in numpy we use the logical and &
teenagers = ages[ages < 18] # teenagers its new array
print(teenagers)
adults = ages[(ages >= 18) & (ages < 65)] # in numpy we use the logical and & 
print(adults)
seniors = ages[ages >= 65]
print(seniors)
evens = ages[ages % 2 == 0]
print(evens)
odds = ages[ages % 2 != 0]
print(odds)

# we can preserve the dimension of the original array that we filter
# we use the where function
# the where function structure : 
# np.where(the condition, our array that we filter, the value that replaces the non filter data)
# for example
qamro = np.where(ages == 18, ages, 0) # here we replace the other values that are different of 18 by 0
print(qamro)
qamro = np.where(ages == 18, ages, -1) # here we replace the other values that are different of 18 by -1
print(qamro)
# NOTE: np.nan indicates a non number value
qamro = np.where(ages == 18, ages, np.nan) # here we replace the other values that are different of 18 by nan
print(qamro)
# if you want the index that satisfy a condition use np.where(only the condition)
# if our array is 1D the output will be the index that satisfy our condition directly
# if our array is 2D the output will be a tuple of two arrays 
# the first array in the tuple shows the row indexes that satisfy our condition
# the second array in the tuple shows the column indexes that satisfy our condition
qamro = np.where(ages == 18) # here we search for the index that satisfy our condition
print(qamro)