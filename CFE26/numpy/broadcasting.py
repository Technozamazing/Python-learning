# Broadcasting allows NumPy to perform operations on Arrays
# with different shapes by virtually expanding its dimensions(smaller one)
# so they matches the larger Array's shape 

# General rule:
# When operating on two arrays, NumPy compares their shapes element-wise,
# starting from the trailing dimesion and working its way left.
# Two dimensions are compatible when:
# --> They are equal or,
# --> Either of them is 1.


# Example of broadcasting with scalars:
import numpy as np

# a = np.array([1, 2, 3])
# b = 3.0
# result = a + b
# print(result)
# # when an array and a scalar is operated, the scalar is stretched to match the 
# # shape of the array



# # Example of broadcasting with Arrays:
# matrix1 = np.array([[1, 2, 3, 4], 
#                     [5, 6, 7, 8], 
#                     [9, 10, 11, 12], 
#                     [13, 14, 15, 16]])

# matrix2 = np.array([1., 2., 3., 4.])
# matrix_sum = matrix1 + matrix2
# print(matrix_sum)

# # here matrix1 is of shape 4x4 and matrix2 is of shape 1x4
# # here row dimension is compatible as one of the dimension is 1
# # also column dimension is compatible as both are same.
# # matrix 2 will be stretched to match the shape of matrix1.






# Here:
array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], 
                   [2], 
                   [3], 
                   [4]])

print(array1.shape)
print(array2.shape)
print('\n')
# here we have !x4 and 4x1 matrices
# so both of them have stretch to match others.
print(array1 * array2)
print('\n')



# Multiplication Table through Broadcasting:
mul1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
mul2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
mul = mul1 * mul2
print(mul)