# Aggregated functions:
# Performs a calculation on set of values (with in given arrays)
# and typically returns a single value.

import numpy as roman

array = roman.array([[1, 2, 3, 4, 5],
                     [6, 7, 8, 9, 10]])


# Aggregated functions:

# for sum of all elements within the array
print(roman.sum(array))

# for arithmetic mean of given array elements
print(roman.mean(array))

# for standard deviation of the distribution
print(roman.std(array))

# for varience of the distribution
print(roman.var(array))

# for "min value" within the given distribution
print(roman.min(array))

# for "max value" within the given distribution
print(roman.max(array))

# for "Position of min_value"
print(roman.argmin(array))

# for "Position of max_value"
print(roman.argmax(array))







# Performing on Axis:
# Here we can select either a row or a column and perform indivisual operation on it.


# sum of columns:
print(roman.sum(array, axis=0))

# Sum of rows:
print(roman.sum(array, axis=1))