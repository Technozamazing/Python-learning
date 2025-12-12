str1 = 'Roman Shrestha is an Engineering major student.'
str2 = "He's studying at Tribhuvan University."

# Concatenation
full_str = str1 + " " + str2
print(f'\nConcatenated String: {full_str}')
print(f'Length of Concatenated String: {len(full_str)}')



# Sequence scapeping characters
escaped_str = 'This is a line with a newline character.\nThis is the second line.'
print(f'\nEscaped String:\n{escaped_str}')

escaped_str = 'This is a line with a newline character.\tThis is the second line.'
print(f'\nEscaped String:\n{escaped_str}')

 

# Multiline String
multiline_str = '''This is a multiline string.
It can span multiple lines.
You can write as much as you want here.'''
print(len(multiline_str))



# String Methods
sample_str = "  Hello, World! Welcome to Python Programming.  "
print(f'\nOriginal String: "{sample_str}"')

print(f'Uppercase: "{sample_str.upper()}"')
print(f'Title Case: "{sample_str.title()}"')      #Each word starts with an uppercase letter
print(f'Capitalized: "{sample_str.capitalize()}"')  #First character uppercase, rest lowercase
print(f'Lowercase: "{sample_str.lower()}"')
print(f'Strip Whitespaces: "{sample_str.strip()}"')          #Remove leading and trailing whitespaces
print(f'Replace "World" with "Universe": "{sample_str.replace("World", "Universe")}')
print(f'Find "Python": {sample_str.find("Python")}')         #Returns the starting index of the substring
print(f'Index of "Python": {sample_str.index("Python")}')    #Returns the index of the first occurrence of the substring
print(f'Split by spaces: {sample_str.split()}')              #Splits the string into a list of substrings
print(f'Count of "o": {sample_str.count("o")}')              #Counts occurrences of a substring
print(f'Starts with "  He": {sample_str.startswith("  He")}')      #Checks if string starts with the given substring
print(f'Ends with "ming.  ": {sample_str.endswith("ming.  ")}')    #Checks if string ends with the given substring
#Here thing to remember is that everything in python is an object.
#So, string is also an object of class 'str' and it has these built-in methods.




#Here is an example of string indexing and slicing:
string_example = "PythonProgramming"
print(string_example[0])        # First character
print(string_example[-11])       # Last character   #Negative indexing
print(string_example[0:6])     # First six characters
print(string_example[2:6])

#Negative Indexing and Slicing
print(string_example[-6:])    # Last six characters
print(string_example[-11:-5])
