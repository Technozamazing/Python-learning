import sys

name = 'Roman Shrestha'
age = 22
height = 5.7  # in feet


print(sys.version) # Print Python version through sys module
# print(f"My name is {name}, I am {age} years old and my height is {height} feet.")


print('My name is',name) # print using commas
print(f'My name is {name}, I am {age} years old and my height is {height} feet.') # print using f strings 
print("My name is {}, I am {} years old and my height is {} feet.".format(name, age, height)) # print using format method       
print("My name is %s, I am %d years old and my height is %.1f feet." % (name, age, height)) # print using % operator
print("My name is " + name + ", I am " + str(age) + " years old and my height is " + str(height) + " feet.") # print using concatenation

# f strings are the most preferred way to format strings in Python 3.6 and above due to their readability and efficiency.