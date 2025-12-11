# Type Conversion
'''Happens Automatically when you perform operations with mixed data types'''

# Type Casting
'''Manually converting one data type to another using built-in functions like int(), float(), str(), etc.'''



# Example of Implicit Type Conversion
x = 5    # x is of type int
y = 5.0  # y is of type float
result = x + y  # x is implicitly converted to float
print(f'Implicit Type Conversion: {result} (type: {type(result)})')  # result is of type float



# Example of Explicit Type Conversion (Type Casting)
a = 10     # a is of type int
b = 3.5    # b is of type float
# Converting float to int 
c = int(b)  # c is now of type int
print(f'Explicit Type Conversion: {c} (type: {type(c)})')

# string and int can't be concatenated directly - done using type casting
str_num = "100"
int_num = 50
# Converting string to int
total = int(str_num) + int_num
print(f'String to Int Conversion: {total} (type: {type(total)})')