# Functions in Python
# Functions are reusable blocks of code that perform a specific task.

# Syntax:
def function_name(parameters):
    """Docstring: Description of the function."""
    # Function body
    # return value  # Optional return statement
    pass # Placeholder for future code



# Example of function:
def greet(name):                                           # parameter 'name' is defined here
    """Function to greet a person with their name."""
    # If I have done this ...
    # greeting = print(f'Hello, {name}!')
    # return greeting
    return f"Hello, {name}!"

greeting = greet('Roman Shrestha')                         # argument 'Roman Shrestha' is passed to the function
print(greeting)  # Output: Hello, Roman Shrestha!



# Function with multiple parameters:
def add_numbers(num1, num2):
    total_sum = num2 + num1
    return total_sum

num1 = int(input(f'Enter the first number: '))
num2 = int(input(f'Enter the second number: '))
total_sum = add_numbers(num1, num2)
print(f'The sum of given numbers is: {total_sum}')


# Function without parameters:
def display_message():
    print('This is a simple function without parameters.')
display_message()


# Function with default parameter value:
def power(base,exponent = 2):
    """Function to calculate power of a number with default exponent as 2."""
    return base ** exponent
pow = power(5) # Using default exponent value as 2.
# Note: Default parameters should always be placed after non-default parameters in the function definition.
print(f'5 raised to the power of 2 is: {pow}')


# WAF to print the length of a list. (list is the parameter):
def length_of_list(mylist):
    return(len(mylist))

mylist = length_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f'Length of the given list is: {mylist}')

# Alternative:
def length_of_list(input_list):
    count = 0
    for val in input_list:
        count += 1
    return count

my_list = length_of_list([10, 20, 30, 40, 50])
print(f'Length of the given list is: {my_list}')


# WAF to print elements of a list in a single line. (list is the parameter):
def elements_of_list(input_list):
    for val in input_list:
        print(val, end = ' ')
    print()    
elements_of_list([1, 2, 3, 4, 5, 5, 6])


# WAF to find the factorial of n. (n is the parameter)
def factorial(num):
    fac = 1
    for i in range(num, 1, -1):
        fac *= i
    return fac
val = int(input('Enter the number to calculate factorial: '))
print(f'Factorial of the given number is: {factorial(val)}')


# WAF to convert USD to NPR:
def currency_converter(input_currency):
    output_currency = 144.47 * input_currency
    return output_currency
usd = int(input('Enter the amount in usd to convert it into npr: '))
print(f'Nepalese currency equivalent of the given US dollars is {currency_converter(usd)}')


# WAF to differenciate odd and even numbers:
def number(input_num):
    if input_num % 2 == 0:
        return f'even'
    else:
        return f'odd'
num = int(input('Enter a number: '))
print(f'Entered number is {number(num)}')


# Note: In Python, functions are first-class citizens, 
# meaning they can be passed as arguments to other functions, 
# returned from other functions, and assigned to variables.

# Lambda Functions (Anonymous Functions):
# They are small, unnamed functions defined using the lambda keyword.
square = lambda x: x ** 2
result = square(5)
print(f'The square of 5 is: {result}')
