import numpy as np 
# git commit -m "aggregation functions"
# aggregate functions is used to summarize data 
# typically aggregate functions return a single value
array = np.array([[1, 2 ,3 ,4, 5],
                [6, 7, 8, 9, 10]])
# sum all the elements in an array function
print(np.sum(array))
# the mean of all the elements in an array function
print(np.mean(array))
# Product (multiplication) of elements
print(np.prod(array))
# Middle value after sorting the array
print(np.median(array))
# calculate Array/Vector/matrix magnitude for all elements in the array
# using this law : sqrt(x² + y² + z² + ....)
print(np.linalg.norm(array))
# calculate Array/Vector/matrix magnitude for all elements in each column
print(np.linalg.norm(array, axis=0))
# calculate Array/Vector/matrix magnitude for all elements in each row
print(np.linalg.norm(array, axis=1))
# Returns the cumulative (running) sum of the elements in the columns
print(np.cumsum(array, axis=0))
# Returns the cumulative (running) sum of the elements in the rows
print(np.cumsum(array, axis=1))
# the standard deviation of elements in an array function (الانحراف المعياري) this is for statistics
print(np.std(array))
# the variance of elements in an array function (التباين) this is for statistics
print(np.var(array))
# the minimum value of all the elements in an array function
print(np.min(array))
# the maximum value of all the elements in an array function
print(np.max(array))
# the position(index) of the minimum value of all the elements in an array function
print(np.argmin(array))
# the position(index) of the maximum value of all the elements in an array function
print(np.argmax(array))
# sum all the columns function
print(np.sum(array, axis=0))
# sum all the rows function
print(np.sum(array, axis=1))
# mean of the columns elements function
print(np.mean(array, axis=0))
# mean of the rows elements function
print(np.mean(array, axis=1))

# generally if we wanna operate with only rows or only columns we add axis=0 for columns and axis=1 for rows
