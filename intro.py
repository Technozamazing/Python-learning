import sys

name = 'Roman Shrestha'
age = 22
height = 5.7  # in feet


print(sys.version) # Print Python version through sys module
# print(f"My name is {name}, I am {age} years old and my height is {height} feet.")

print('')
print('My name is',name) # print using commas
print(f'My name is {name}, I am {age} years old and my height is {height} feet.') # print using f strings 
print("My name is {}, I am {} years old and my height is {} feet.".format(name, age, height)) # print using format method       
print("My name is %s, I am %d years old and my height is %.1f feet." % (name, age, height)) # print using % operator
print("My name is " + name + ", I am " + str(age) + " years old and my height is " + str(height) + " feet.") # print using concatenation

# f strings are the most preferred way to format strings in Python 3.6 and above due to their readability and efficiency.

wealth1 = True
wealth2 = False
wealth3 = None

# print(f'Is he rich? {rich}')
print('')
print(f'Is he wealthy? {wealth1}')
print(f'Is he poor? {wealth2}')
print(f'Is his wealth status known? {wealth3}')

print('')
print(type(name))  #<class 'str'>
print(type(age))  #<class 'int'>
print(type(height))  #<class 'float'>
print(type(wealth1))  #<class 'bool'>
print(type(wealth3))  #<class 'NoneType'>


# Example of f-string
value = 'roman'
txt = f'My name is {value}'
print('\n' + txt  )

var = value*2
output = (value + '2')*4  # Multiplying string by integer repeats the string

print(output)
print(type(output))
print(age**3)  


# Python is an Implicit type Language
x = 5       # x is of type int  
print(type(x))
x = "Hello" # x is now of type str