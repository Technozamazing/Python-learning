# This is the beginning of this file
# Its contains all the thing related to Python problems done during Campus Lecture.



# WAP to find the number is +ve, -ve or zero

num = int(input("Enter a Number:"))
if num > 0:
    print(f"Entered number {num} is Positive")
elif num < 0:
    print(f'Entered number {num} is Negative')
else:
    print("Entered number is 0")



# WAP to ask the person age. If they are 18 or older print -- You are adult, else print -- You are minor
age = int(input("Enter age of a person: "))
if age >= 18:
    print('You are an Adult')
elif age <18:
    print('You are a Minor')



# check if the user input username and password is correct or incorrect:

userName = input("Enter Your Username: ")
password = input("Enter Your Password: ")

originalUser = "roman"
originalPass = "roman"

if originalUser == userName and originalPass == password:
    print("Login Successful!")
else:
    print("Invalid Username or Password!")









# Python Lab: 01
# 1. WAP that accepts a student''s name , roll number and marks of three subjects. Calculate the average and print the student details along with the average marks.
name = input(f"Enter Student's Name: ")
sub = ["Maths", "Science", "English"]
rollNumber = input("Enter Student's Roll Number: ")
marks = []

for i in range(3):
    mark = float(input(f"Enter Marks in {sub[i]}: "))
    marks.append(mark)

average = (marks[0] + marks[1] + marks[2]) / 3

print(f"\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {rollNumber}")
print(f"Average Marks: {average}")



# 2. WAP to determine whether a given year is a leap year or not.
year = int(input("Enter a Year: "))
if year % 400 == 0 or year % 4 == 0:
    print(f'Entered year {year} is a Leap year.')
else: 
    print(f"Entered year {year} is not a Leap year.")



# 3. WAP that takes a number as input. If the number is divisible by 2,3 and 5 at the same time, print "Super Divisible", else  print which of the number it is divisible by.
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print(f'Nmber {num} is Super Divisible.')
else:
    print(f'Number {num} is not Super Divisible.')
    # for i in range
    num = 1
    test = num % 2 == 0 and num % 3 == 0 and num % 5 == 0
    while not test:
        num += 1
        test = num % 2 == 0 and num % 3 == 0 and num % 5 == 0
    print(f'Next Super Divisible number is {num}')



# 4. Develop a Python program to print numbers from 1 to 50.
#    The program should skip all the numbers that are divisible by 5 using the continue statement.
for i in range(1, 51, 1):
    if i % 5 != 0:
        print(i)



# 5. WAP to takes numbers continuously from the user until the user enters 0. For each  number entered, displey wheather it is even or odd.
while True:
   num = int(input(f'Enter a number: (Zero to exit.)'))
   if num == 0:
       print('You have entered Zero.')
       break
   elif num % 2 == 0:
       print(f"{num} is even.")
   else:
       print(f"{num} is odd.")



# 6. WAP to repaetly ask user to enter a password until the correct password is entered. 
#    Print "Access Granted" when the correct password is entered.
correct_password = "admin123"
while True:
    password = input("Enter a password: ")
    if correct_password == password:
        print("Access Granted!")
        break
    else:
        print("Incorrect Password!\nTry Again!")



# 7. WAP that takes two numbers from the users. Keep taking the  numbers until the user enters both zeros
#    print the smallest each time.
while True:
    num = []
    for i in range(2):
        while True:
            try:
                number = int(input(f'Enter the {i+1} number: '))
                num.append(number)
                break
            except ValueError:
                print("\nInvalid Input!\nEntered number should be Integer!\n")

    if num[0] == num[1] == 0:
        print("Both entered numbers are Zeros.")
        break
    elif num[0] > num[1]:
        print(f'{num[0]} is greater than {num[1]}.\n')
    elif num[1] > num[0]:
        print(f"{num[1]} is greater than {num[0]}.\n")
    else:
        print("Both are Equal!\n")


# 8. WAP that keeps asking the users to enter a number until 0 is entered.
#    Print "Valid range" if 1 -- 100. else "Out of range"

while True:
    while True:
        try:
            num = int(input("Enter a number between 1 to 100: "))
            break
        except ValueError:
            print("\nInvalid Type!\nEntered number should be an Integer.\n")
    
    if num == 0:
        print("Entered number is Zero.")
        print("Exiting...\n")
        break
    elif num <= 100 and num >= 1:
        print("Valid Range!\n")
    else:
        print("Out of Range!\n")



# 9. WAP using while loop that keeps asking the user to enter a number.
#    If the user enters -- 0,  the program should exit the loop using break.
#    If the users enters a negative number, the program should skip the current
#    iteration using continue statement. Otherwise print the number.

while True:
    while True:
        try:
            num = int(input("Enter a number (Zero to exit): "))
            break
        except ValueError:
            print("Invalid Input!\nEntered number should be an Integer.\n")
    if num == 0:
        print("Entered number is Zero.\nExiting the program...\n")
    elif num < 0:
        continue
    else:
        print(num, "\n")
    










# Lab 02:
# Write a function calculate_bmi() that takes weight (kg) and height (m) as 
# parameters, calculates BMI using formula: 
# BMI = weight / (height²). 
# Then, it returns 
# BMI rounded to 2 decimal places. Include error handling for zero or negative inputs.
def validate_input(height, weight):
    if height < 0 and weight < 0:
    
        raise ValueError("Height and Weight cannot be negative!")
    elif height < 0:
        raise ValueError("Height cannot be negative!")
    elif weight < 0:
        raise ValueError("Weight cannot be negative!")
    
def cal_bmi(weight, height):
    bmi = weight/(height**2)
    return float(bmi)

try:
    height = int(input(f'Enter your height: '))
    weight = int(input(f'Enter your weight: '))
    validate_input(height, weight)
    bmi = cal_bmi(weight, height)
    print(f'Your BMI is {bmi:.2f}\n')
except ValueError as e:
    print(f'Error: {e}')
except Exception as e:
    print(f'An unexpected error occurred: {e}')

# Conclusion of the problem:
# We can define our own custom exception handling for the runtime error.




# Create a function string_operations() that accepts a string as input and returns a 
# tuple containing: the string in uppercase, the string in lowercase, the string with first 
# letter capitalized, the string reversed. For eg. "Hello" → ("HELLO", "hello", "Hello", "olleH")
def string_operations(string_in):
    str_upper = string_in.upper()
    str_lower = string_in.lower()
    str_capital = string_in.capitalize()
    str_reversed = string_in[::-1]
    return (str_upper, str_lower, str_capital, str_reversed)

input_string = input("Enter a string: ")
result = string_operations(input_string)
print(f'Resulting tuple: {result}') 

# Conclusion:
# We have created a function that performs multiple string operations and returns the results as a tuple.






# Implement a function process_numbers() that accepts a "variable number of numeric arguments" 
# using "*args"  -->  returns a dictionary with: 
# 'sum': total of all numbers, 'average': mean of numbers, 'max': maximum value, 'min': minimum value.  
def process_numbers(*args):
    total = sum(args)
    print(type(args))
    average = total / len(args) if args else 0
    maximum = max(args) if args else None
    minimum = min(args) if args else None
    return {
        'sum': total,
        'average': average,
        'max': maximum,
        'min': minimum
    }

numbers = [10, 20, 30, 40, 50]
result = process_numbers(*numbers)  
print(f'Processed numbers: {result}')

# Conclusion:
# From this program we have learned how to use *args to accept variable number of arguments in a function.




# Write a function validate_email() that takes an email address as parameter, returns 
# True if email is valid (contains '@' and '.', '@' not first/last), returns False otherwise. 
# Use only string methods 
def validate_email(email):
    if "@" in email and "." in email:
        at_index = email.index("@")
        dot_index = email.rindex(".")
        if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
            return True
    return False

email_input = input("Enter an email address: ")
if validate_email(email_input):
    print("Valid Email Address.")   
else:
    print("Invalid Email Address.")












# Lab 03:
# Given a list numbers = [5, 2, 8, 1, 9], write code to sort it in ascending order. 
num = [5, 2, 8, 1, 9]
num.sort()
print(num)


# Create a new list containing only even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
Original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
for num in Original:
    if num % 2 == 0:
        even.append(num)

print(even)


# from list comprehension:
# new_list = [expression for item in iterable if condition]
given = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [num for num in given if num % 2 == 0]
print(even)





# Write a program that takes two lists of equal length and returns a new list where 
# each element is the sum of the corresponding elements from the input lists, then 
# extend this to handle lists of unequal length by padding the shorter list with zeros. 
list1 = [1, 2, 3, 4, 9]
list2 = [5, 6, 7, 8, 1, 1]
# add_list = [x + y for x, y in zip(list1, list2)]     -- List Comprehension of the bellow 
add_list = []
for num, elem in zip(list1, list2):
    add_ls = num + elem
    add_list.append(add_ls)
print(add_list)



# Extending the smaller list by 0s.
list1 = [1, 3, 4, 6, 7]
list2 = [3, 2, 5, 7, 4, 6, 7]
if len(list1) > len(list2):
    diff = len(list1) - len(list2)
    for i in range(0, diff):
        list2.append(0)
if len(list2) > len(list1):
    diff = len(list2) - len(list1)
    for i in range(0, diff):
        list1.append(0)
add_list = [x + y for x, y in zip(list1, list2)]
print(add_list)

# zip:
# The zip() function in Python combines elements from multiple iterables (like lists, tuples, strings) 
# into tuples, pairing elements by their position. It stops when the shortest iterable is exhausted.





# Dictionary Operation:

# Create a dictionary representing a book with keys for title, author and year.
book = {
    'title': 'Karnali Blues',
    'author': 'Buddhisagar',
    'published_year': 2010
}
print(book)
print(type(book))


# write a code to add a new key-value pair  "price":200  to an existing dict.
book["price"] = 200
print(book)


# create a dictionary that counts how many times each letters appears in the word "hello".
word = 'Hello'
letter_count = {}
for ch in word:
    letter_count[ch] = letter_count.get(ch, 0) + 1
print(letter_count)

# # letter_count = {ch: "hello".count(ch) for ch in set("hello")}

# from collections import Counter         # Counter is a special dictionary. It counts how many times each element appears in a list.
# letter_count = Counter('Hello')
# print(letter_count)


# Write a function called invert_dictionary that takes a dictionary and returns a new 
# dictionary where keys and values are swapped, handling collisions by storing the 
# original keys as a list of values for any duplicate values in the input.
def invert_dictionary(d):
    inverted = {}
    
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    
    return inverted

val = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 1
}
print(invert_dictionary(val))


#  Create a function named deep_merge that recursively merges two nested 
# dictionaries, combining their contents such that if the same key exists in both, the 
# values are merged recursively if they are dictionaries, otherwise the value from the 
# second dictionary overwrites the first. 
def deep_merge(dict1, dict2):
    result = dict1.copy()  # avoid modifying the original dict1
    
    for key, value in dict2.items():
        if (
            key in result
            and isinstance(result[key], dict)
            and isinstance(value, dict)
        ):
            # Recursively merge nested dictionaries
            result[key] = deep_merge(result[key], value)
        else:
            # Overwrite or add new key
            result[key] = value
    
    return result
d1 = {
    "a": 1,
    "b": {"x": 10, "y": 20},
    "c": 3
}

d2 = {
    "b": {"y": 99, "z": 30},
    "c": 100,
    "d": 4
}
print(deep_merge(d1, d2))




# Comprehension:

# use list comprehension to create a list of squares for numbers 1 through 5.
num = list(range(1, 6))
sqr = [x**2 for x in num]
print(sqr)


# use dict comprehension to create a dictionary where keys are numbers 1-3 and values are their doubles.
double = {i:i*2 for i in range(1, 4)}
print(double)


# Use list comprehension to extract all vowels from the string "python programming".
vow = [ch for ch in 'python programming' if ch in 'aeiou']
print(vow)


#  Write a function called calculate_statistics that accepts a list of numbers and 
# returns a dictionary containing the mean, median, and mode of those numbers, 
# ensuring you handle edge cases like empty lists or single-element lists. 
from collections import Counter

def calculate_statistics(numbers):
    # Edge case: empty list
    if not numbers:
        return {"mean": None, "median": None, "mode": None}
    
    n = len(numbers)
    sorted_nums = sorted(numbers)
    
    # Mean
    mean = sum(numbers) / n
    
    # Median
    if n % 2 == 1:
        median = sorted_nums[n // 2]
    else:
        median = (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2
    
    # Mode
    freq = Counter(numbers)
    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]
    
    # If all values appear once, there is no mode
    mode = modes[0] if max_freq > 1 else None
    
    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }

numbers = [1, 2, 3, 3, 3, 3, 4, 4, 5, 6, 2, 4, 1 , 6, 9, 9, 6, 5, 2, 4, 1, 0]
print(calculate_statistics(numbers))