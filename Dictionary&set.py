# Dictionary in Python:
# Dictionary are used to store data values in "key:value" pairs

# They are unordered (unlike: string, list and tuple) -- meaning no indexing.
# They are mutable (changeable) -- can be changed later.
# Duplicate keys aren't allowed.


# Example:
person = {
    "name": "Roman Shrestha",
    "is Adult": True,                             #Boolean Type
    "Semester|Year": "III|I",
    "sub": ["math", "physics", "computer"],       #List Type
    "topics": ("dict", "set")                     #Tuple Type
}

print(type(person))
print(person["name"])
print(person["sub"])

# Creating a new key:value pair
person["has girlfriend"] = False
print(person)

# Reassigning key value:
person["name"] = "Roman"
person["surname"] = "Shrestha"
print(person)


# Null Dictionary:
null = {}
null["name"] = "Sabin Ojha"
null["age"] = 21
null["is_Male"] = False
print(null)


# Nested Dictionary:
student = {
    "name": "Sagar Panth",
    "score": {                # score dictionary inside student dictionary
        "Mathematics": 50,
        "Physics": 48,
        "Drawing": 20,
        "Fundamental of Electronics and Electrical": 51,
    },
    "id": "PAS080BEI028",
}
print(student["score"])
print(student["score"]["Physics"])  # Way to access nested data.




# Like methods in string, list and tuple
# Dictionary Methods:
# person.keys() -- returns all keys
# person.values() -- returns all values
# person.items() -- returns all "(key,value)" pairs as tuples
# person.get("key") -- returns the key's to value equivalent to "person("key")"
# person.update() -- store new key-value pair in the current dictionary.

print(student.keys())
# Converting it into normal list or tuple through type casting.
print(list(student.keys()))
print(tuple(student.keys()))
print(f'Total number of key value pairs: {len(student.keys())}')

print(type(list(student.values())))

data = list(student.items())
print(data[0])


# When both student.get("key") and student["key"] returns the same value
# why to use student.get("key")?
# Simple answer is -- why we try to access key value of undefined key
# Our traditional method (student["key"])  will throw error interuting the normal program flow then after
# But student.get("key") -- will return none -- thus not affecting the normal flow then after.


# Example:
print(student.get("name"))
print(student.get("room")) # --> will return "None" without affecting flow
# print(student["room"]) # --> will throw error "KeyError" -- affecting programs then after.


# Store new key_value pair in the dictionary:
student.update({"is_Male": True, "lives_in_Kathmandu": False})
print(student)



# Store following word meanings in a python dictionary
# table: "a piece of furniture", "list of facts and figure"
# cat: "a small animal"
Dictionary = {}
value = {"cat":"a small animal", "table":("a piece of furniture","list of facts and figure")}
Dictionary.update(value)
print(Dictionary)


# WAP to enter marks of 3 subjects from the user and store them in dictionary.
# Start with an empty dictionary and add one by one. Use subject name as key and marks as value.











# Set in python:
# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable(boolean, int, float, string, tuple)
# Remember that: Set as a whole is mutable but its content/element is immutable unlike in Dictionary where elements can be changed. 
 
collections = {1, 2, 3, 4, 4, "Roman", "Sagar", "Roman"}
print(type(collections))
print(len(collections))
print(collections)


# Creating a empty set:
# new = {}  --  This will create a empty Dictionary not a set.
new = set()  # --> will create a empty set.


# Methods in Set:
# 1. set.add(el)  --> adds an element
# 2. set.remov(el)  --> removes the el -element from the set
# 3. set.clear()  --> empties the set
# 4. set.pop()  --> removes a random element from the set.
# 5. set.union(set2)  --> combines both set values and returns new set
# 6. set.intersection(set2)  --> combines common values and returns new set

new.add("roman")
new.add("shrestha")
new.add("coding")
print(new)
new.remove("coding")
print(new)
# new.clear()
# print(new)
# value = new.pop()
# print(value)
print(new)

old = set()
old.add("roman")
old.add("pashchimanchal")
set1 = new.union(old)
print(set1)
set2 = new.intersection(old)
print(set2)
print(set1,set2)



# Let's practice:
# You are given a list of subjects for students. Assume one classroom is required for
# one subject. How many classrooms are needed by all students
# "python", "java", "javascript", "c", "python", "java"
# Hint: set removes dublicate values

sub = {"python", "java", "javascript", "c", "python", "java"}
print(f'Classrooms needed is {len(sub)}')


