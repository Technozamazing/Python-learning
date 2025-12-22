# Upto now we have studied about the List(Similar to Array)
# We were able to know how string is immutable while list are mutable 
# Knowing that List are mutable,  
# There will be certain situation where we will not want that our list gets changes later on
# For this purpose we introduce Tuples - its like list - the only difference is they are immutable and are inclosed in ()
# Remember that tupes are also built-in data types.


fruits = ['Apple', 'Banana', 'Orange', 'Mango']
print(type(fruits))

fruits = ('Apple', 'Banana', 'Orange', 'Mango')       # Created Tuple as we previously created List
print(type(fruits))



# Accessing Tuple items
print(f"Element inside tuple at index '3' is: {fruits[3]}")
print(f"Element inside tuple at index '-1' is: {fruits[-1]}")   #Negative Indexing



# Slicing in Tuple as in list and 
fruits[:3]  # Slicing first three items
print(f'Fruits from index 0 to 2: {fruits[0:3]}')
print(f'Fruits from last 3 items: {fruits[-3:]}')



# Trying to change the element of tuple
# fruits[1] = 'Tomato'   # This will raise an error because tuples are immutable



# Tuple Methods
print(f'Count of "Apple" in tuple: {fruits.count('Apple')}')  #Counts occurrences of a given element
print(f'Index of "Orange" in tuple: {fruits.index("Orange")}')  #Returns the index of the first occurrence of the given element


# WAP to count the number of students with the "A" grade in the following tuple
# grades = ('A', 'B', 'C', 'A', 'D', 'A', 'B', 'C')
# Hint: use count() method of tuple

Grades = ('A', 'B', 'C', 'D', 'A', 'A', 'F')
print(f'Number of students with grade "A" is: {Grades.count('A')}')


# Storing above values of tuple in list and sorting them from A to D:
marks = []
for i in range(len(Grades)):
    grade = Grades[i]
    marks.append(grade)

print(f'List formed from the given tuple is: {marks}')