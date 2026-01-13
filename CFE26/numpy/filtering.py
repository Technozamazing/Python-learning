# Filtering:
# Refers to the process of selecting elements from an array that matches a given condition.

# Filtering in NumPy means selecting elements from an array that meet certain conditions, 
# producing a new array with only those elements.
# This is typically done using boolean indexing.

# Note: Boolean indexing will return "flatten" array
# To preserve the order/shape of the array to match original we use "where" attribute.


import numpy as np
arr = np.array(["Roman", "Shrestha", "is", "Gay", "Hero"])
x = [True, True, True, False, True]

new_arr = arr[x]
print(new_arr)
# The new array contains only the values where the filter array had the value True(boolean indexing), in this case, 
# index 0, 1, 2 and 4.




# Creating filter array:
# In the example above we hard-coded the True and False values, 
# but the common use is to create a filter array based on conditions.

# odd filter array
arr = np.array(range(1, 21, 1))
odd_arr = arr[arr %2 != 0]
print(odd_arr)  


# marks obtained by students of BEI and BCT in a sub:
marks = np.array([[16, 24, 30, 10, 50, 55],
                 [22, 34, 55, 60, 13, 6]])
fail = marks < 24
print(fail)
failed_marks = marks[fail]
print(failed_marks)

avg = marks.mean()
print(avg)
means = np.mean(marks)
print(means)

deviation = marks.std()
print(deviation)
sd = np.std(marks)
print(sd)

avg_marks = marks[(marks >= (means - sd)) & marks <= (means + sd) ]
print(avg_marks)





# Upto now we have learned that boolean indexing return flatten array - 1D irrespective of original size.
# to maintain the array shape
# we use "where" attribute/function 

# Syntax:
# np.where(condition, array, fill_value)
# any element that don't match the condition is assined the fill_value

passed_students = np.where(marks>=24, marks, "NQ")
print(passed_students)