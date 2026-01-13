import numpy as np

print(np.__version__)


# Basic Operations
py_list = [1, 2, 3, 4]
py_list *= 2
print(py_list)
print(type(py_list))

np_array = np.array([1, 2, 3, 4])
np_array *= 2
print(np_array)
print(type(np_array))





# Multidimensional Arrays
# Arrays are for n-dimensions --> 0d, 1d, 2d, 3d, .... , nd

array = np.array('A')                 
print(array.ndim)                     # 0d array

array = np.array(['A', 'B', 'C'])      
print(array.ndim)                     # 1d array

array = np.array([['A', 'B', 'C'], 
                  ['D', 'E', 'F']])
print(array.ndim)                     # 2d array

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])
print(array.ndim)                     # 3d array
print(array.shape)                    # Shape of the 3d array (depth, rows, columns)
print(array.size)





# Array Attributes
array = np.array([[1, 2, 3], 
                  [4, 5, 6]])
print(array.shape)                # Shape of the array  (rows, columns)  in Tuple format
print(array.size)                 # Total number of elements
print(array.dtype)                # Data type of the elements
print(array.ndim)                 # Number of dimensions
print(array.itemsize)             # Size of each element in bytes
print(array.nbytes)               # Total size of the array in bytes (itemsize * size)
print(array.T)                    # Transpose of the array

# Reshaping Arrays
print(array.flatten())            # Flatten the array to 1D
print(array.reshape(3, 2))        # Reshape the array to 3 rows and 2 columns
print(array.reshape(-1))          # Reshape to 1D using -1     ==    array.flatten()
print(array.reshape(1, 6))        # Reshape to 1 row and 6 columns
print(array.reshape(6, 1))        # Reshape to 6 rows and 1 column




# Chain indexing
print(array[0][0])
print(array[0, 0])                # Better way to index --> multidimensional indexing




# Slicing Arrays
print(array[:, 1])                # All rows, 2nd column
print(array[1, :])                # 2nd row, all columns
print(array[1, 1:3])             # 2nd row, columns from index 1 to 2
print(array[:, :, 2])             # All depth, all rows, 3rd column


matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [10, 11, 12, 13],
                   [14, 15, 16, 17]])

print(matrix[:2, :2])
print('\n')
print(matrix[:2, 2:])
print('\n')
print(matrix[2:4, :2])
print('\n')
print(matrix[2:4, 2:4])
print('\n')
print(matrix[1:3, 1:3])






# Arithematic Operations

# Basic scaler arithematics
scalar = np.array([1, 2, 3, 4])
print(scalar + 1)
print(scalar - 1)
print(scalar / 2)
print(scalar * 2)
print(scalar ** 2)
print('\n')



# Vectorized math functions
nums = np.array([1.2, 2.5, 3.99])
print(np.sqrt(nums))
print(np.round(nums))     # round to nearest
print(np.floor(nums))     # round down
print(np.ceil(nums))      # round up
print(np.pi)



# Give an array of radii of three circles -- find the are of each circle
radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)
print('\n')



# Element-wise Arithematic:
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
print(array1 + array2)
print(array2 - array1)
print(array1 * array2)
print(array2 / array1)
print(array1 ** array2)



# Comparison Operator
scores = np.array([60, 82, 47, 100, 78])
print(scores == 100)       # Topper
print(scores >= 60)        # Passes
print(scores < 60)         # Failed

scores[scores < 60] = 0                 # Sub-script operator
print(scores)