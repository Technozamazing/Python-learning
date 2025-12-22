# # File handling in Python:
# # Python can be used to perform operations on a file. (read, write or append, etc)
# # Types of file:
# # 1. Text files: '.txt', '.log', '.docx'
# # 2. Binary files: '.mp4', '.mov', '.png', '.jpeg'
# '''
# # Recall:
# # In C we use to have file's pointer variable - which initially points to the memory location at 
# # the beginning of a file and performs actions 

# # Python does not have an explicit pointer concept like in C or C++, but it uses a similar mechanism called object references. 
# # In essence, every variable in Python acts as a reference (or pointer) to an object stored in memory. 

# # Here are the key differences and concepts:
# # 1. Variables as Labels/References: 
# #    In Python, variables are not like memory "buckets" that contain data; 
# #    Variables are more like labels or names that point to objects(integer, string, list, everything is an object in python) in memory.
# # 2. Automatic Memory Management: 
# #    Python handles memory management automatically through a garbage collector, which removes the need for manual memory 
# #    allocation/deallocation or explicit pointer arithmetic (like adding or subtracting from memory addresses).
# # 3. No Pointer Arithmetic: 
# #    You cannot perform arithmetic operations on these references. 
# #    This design choice prevents many common memory-related errors such as buffer overflows.
# # 4. Mutable vs. Immutable Types: 
# #    The behavior of "passing" variables is affected by whether the object is mutable 
# #    (like lists and dictionaries) or immutable (like integers, floats, and strings):
# #    1. Mutable objects (lists, dictionaries, etc.) can be changed in place, and all 
# #       variables referencing that same object will see the change. This behavior is similar to how pointers work in C++.
# #    2. Immutable objects (integers, strings, etc.) create a new object when their value is modified, 
# #       and the variable name is simply reassigned to this new object. 
# '''

# # Syntax:
# # # File initialization and opening:
# f = open("demo.txt","r")
# # # File operation:
# data = f.read()
# print(type(data))
# print(f'Data contained in file: \n{data}')
# # # File closing
# f.close
# # # Here close, open, read are all methods of file.




# # Reading a file:
# # 1. data = f.read()        - reads entire file
# # 2. data = f.readline()    - reads one line at a time.

# # print first five letters of file:
# f = open("demo.txt","r")
# data = f.read(5)  # grabs first five characters from the file.
# print(f'Data contained in the file:\n{data}')
# f.close

# f = open("demo.txt","r")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()

# print(line1)
# print(line3)



# # Writing to a file:
# # 1. f = open("demo.txt","w")  - write mode (overwrites the entire file.)
# #    f.write("something...")  

# # 2. f = open("demo.txt"."a")  - append mode (writes from EOF)
# #    f.write("something...")  


# # Using append:
# f = open("demo.txt","a")
# f.write("\nI'm learning Python Today!\nWill deepdive into machine learning after learning python.")
# f.close



# # Multiple modes:
# # 1. Read + Write = "r+"  pointer at beginning  --  will truncate or replace the first len("input_string") character after the pointer.
# #                                               --  will not create a new file, if mentioned file doesn't exits -- it will throw "FileNotFoundError"
# f = open("sample.txt","r+")
# f.write("Hello")
# print(f'\n{f.read()}')
# f.close

# # 2. Write + Read = "w+"  always pointer at BOF  --  Overwrites if file exist
# #                                                --  Create new file of specified name if file doesn't exist.
# f = open("demo.txt","w+")
# f.write("w+ will overwrite all existing content in the file.\nThe only benefit of using 'w+' is that we can also perform read() operation.")
# f.close
# # w+ == +w
# f = open("sample.txt","+w")
# print(f'{f.read()}')

# f = open("sample.txt","+w")
# f.write("This is a sample file for learning.")
# f.close

# # 3. Read + Write = "a+"  pointer at EOF  --  Doesn't overwrites.
# #                                         --  File is created if it doesn't exist.
# f = open("sample.txt","a+")
# # f.seek(0)
# print(f'{f.read()}')
# f.write("\nThis is the second line.")
# f.close

# # Conclusion: "a+" mode isn't that usefull, as the pointer is always at EOF - so it can read the file but it will return always empty.
# # Key takeaway:
# # -- "a+" = read + append
# # -- Pointer starts at EOF
# # -- Use "seek(0)" if you want to read existing content.
# # -- seek(index) = makes the pointer variable point at the given "index"

# f = open("Sample.txt","a+")
# f.seek(0)
# print(f'{f.readline()}')
# f.close


# # There is a better way to write file code in python with:
# # with Syntax

# with open("sample.txt","r") as f:
#     # Here f is an alice for open()
#     data = f.read()
#     print(data)
#     # Closing statement is already included in "with" -- no need to close the file.

# with open("sample.txt","w") as f:
#     f.write("Everything is wiped out!")







# # Deleting a file:
# # using the os module  
# import os
# os.remove("delete.txt")




# # Let's Practice:
# # 1. Create a new file "practice.txt" using python. Add the following data in it:
# # Hi everyone 
# # we are learning File I/O 
# # using java. 
# # I like programming in java.
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\nusing Java.\nI like programming in Java.")

# # 2. WAF that replaces all occurrence of "java" with "python" in above file.
# with open("practice.txt","r+") as f:
#     content = f.read()
#     new_content = content.replace("Java", "Python")
#     print(new_content)
#     f.seek(0)
#     f.write(f'{new_content}')

# # 3. Search if the word "learning" exist in the file or not.
# # with open("practice.txt","r+") as f:
# #     string = f.read()
# #     search = string.find("Python")
# #     print(search)
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find("learning") != -1):
#         print("Found")
#     else:
#         print("Not Found")


# 4. WAF to find in which line of the file does the word "learning" occur first.
# print -1 if word not found.

# def check_in_line():
#     line_var = 0
#     word = "learning"
#     found = False
#     with open("practice.txt","r") as f:
#         while True:
#             line = f.readline()
#             line_var += 1
#             if (line.find(word) != -1):                         # Can also: if word in line:
#                 print(f'Found "{word}" at line {line_var}.')
#                 found = True
#                 break
#     if found != True:
#         print(f'"{word}" not found!')

# Defects in this code:
# Infinite loop risk
# 1. When readline() reaches EOF, it returns an empty string "".
#    Your while True" never checks for this → infinite loop.
# 2. Line count increments even at EOF
#    line_var is incremented before checking whether a line exists.
# 3. Function does not print -1 as required
#    The question says print -1 if word not found.
# 4. Unnecessary found flag
#    You can simplify the logic.

# Revised version of above code:
def check_in_line():
    line_var = 0
    word = "Python"

    with open("practice.txt","r") as f:
        while True:
            line = f.readline()
            if(line == " "):
                break

            line_var += 1
            if word in line:      
                print(f'Found "{word}" at line {line_var}')
                return
    print("Not found")

check_in_line()
# Check the file "test.py" you will find something funny!


# Finding from above solution: 
# EOF is represented by = when pointer returns empty space (" ").
# We can use "word in line" instead (more readable)
# "in" is a membership operator & returns boolean
# Example:


# Solve this problems later...
# 5. From a file containing numbers separated by comma, print the count of even numbers.

