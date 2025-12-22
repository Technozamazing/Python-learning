# Lists are similar to Arrays in other languages 
# They are used to store multiple items in a single variable
# Remember that lists are mutable unlike strings which are immutable, meaning you can change the elements of a list after its creation.
# Remember that list are built-in data types.

# Creating a List
fruits = ['Apple', 'Banana', 'Orange', 'Mango']
print(f'Fruits List: {fruits}')
# print(len(fruits))

# for fruits_item in fruits:
#     print(fruits_item)
# # Accessing List Items

for i in range(4):
    print(f'Fruit at index {i+1}: {fruits[i]}')




# How is string immutable but list is mutable?
# for example:
my_string = 'Hello'
print(my_string[2])  # Output: l
# Instead if we try
# my_string[2] = 'x' # This will raise an error because strings are immutable

# Where as in List we can change the elements of list whenever we want.
# From our previous fruits list:

print(f'Original Fruits List: {fruits}')    # Output: ['Apple', 'Banana', 'Orange', 'Mango']
fruits[1] = 'Tomato'  # This will change 'Banana' with 'Tomato'.
print(f'Modified Fruits List: {fruits}') 


# Adding 4 new fruits to fruits-list from user
for i in range(4):
    new_fruit = input('Enter a fruit to add to the list: ')
    fruits.append(new_fruit)   # append() method is used to add an item to the end of the list.

print(f'Updated Fruits List: {fruits}')


# Slicing in list
print(f'Fruits from index 1 to 4: {fruits[1:7]}')  
print(f'Fruits from last 4 items: {fruits[-4:]}')



# Similar to methods(functions) in string we have methods in list as well.
fruits.append('Pinapple')   # Adds 'Pinapple' at the end of the 
print(f'Fruits list after Append: {fruits}')
fruits.insert(0, 'Peach')   # Insert element at given index
print(f'Fruits list after insert: {fruits}')
number = [2,3,1,6,5,4]
number.sort()
fruits.sort()
print(f'Sorting in Ascending order: {number}')
print(f'Sorting in ascending order: {fruits}')
fruits.sort(reverse = True)
print(f'Sorting in descending order: {fruits}')
number.reverse()   # Reverses the current order of the list
print(f'given number list in reverse order: {number}')

print(f"First occurrance of '6' is at {number.index(6)}")


# Methods for removing elements from the 
num = [1,3,1,2,3,4,6,5]
num.remove(1)   # remove first occurrence of the given element
print(f"num list after removing 1st '1': {num}")

num.pop(3)    # remove element from given index
print(f'Final num list: {num}')
print(type(num))


# Clearing the entire list
num.clear()
print(f'num list after clearing all elements: {num}')


# Copying a list
new_fruits = fruits.copy()
print(f'Copied fruits list: {new_fruits}')


# Joining two lists
vegetables = ['Carrot', 'Potato', 'Cabbage']
all_foods = fruits + vegetables
print(f'All foods list (fruits + vegetables): {all_foods}')


# WAP to ask the user to enter names of their 3 favourite movies and store them in list
movies = []
print(f'{type(movies)}\n')

for i in range(3):
   fav_movies = input(f'Enter your {i+1}th favourite movie: ')
   movies.append(fav_movies) 

print(f'\nYour favourite movies are: {movies}\n')


# WAP to check if a list contains a palindrome of elements.
# Hint: use copy() and reverse() methods of list

original_list = [1,2,3,4,2,1]
str = "madam"
# copy_str = str.copy()
# print(f'{copy_str}')     # AttributeError: 'str' object has no attribute 'copy'
copy_list = original_list.copy()
print(f'{copy_list}')
original_list.reverse()
print(f'The given list is Palindrome') if copy_list == original_list else print(f'The given list is not Palindrome')