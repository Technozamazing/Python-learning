# How to take input from user and display output in Python

'''
input() function is used to take input from user in Python.
By default, input() function takes input as 
for other input types -- we use type casting functions like int(), float(), etc.

# for string input
name = input("Enter your name: ")
print(f'Hello, {name}!')

# for integer input
age = int(input("Enter your age: "))
print(f'Your age is {age} years old.')

# for float input
height = float(input("Enter your height in feet: "))
print(f'Your height is {height} feet.')

'''

import sys

name = input("Enter your name: ")
print(f'Hello, {name}!')

age = int(input("Enter your age: "))
print(f'Your age is {age} years old.')

height = float(input("Enter your height in feet: "))
print(f'Your height is {height} feet.')