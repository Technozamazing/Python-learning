# In Python, try and except blocks are used for exception handling, allowing your program to 
# continue running even if an error occurs. 

# Python provides two additional optional blocks to give you complete control over the process:
# 1. try: This block contains the code that might raise an exception.
# 2. except: This block contains the code that runs if an exception occurs in the try block.
# 3. else: This block runs if no exceptions were raised in the try block.
# 4. finally: This block always runs, regardless of whether an exception occurred or not.


balence = 2400
while True:
    try:
        deposite = int(input("Enter the amount to deposit: "))
        break
    except ValueError:
        print(f'\nError: Invalid Type!\nPlease enter a valid integer.\n')

balence += deposite
print(f'Balence: {balence}')




# else and finally case block example
try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input, Please enter a valid integer.")
else:
    print(f'Result: {result}')         # Only runs if no exception occurs in try block
finally:
    print("Execution Completed.")      # Always runs regardless of exceptions    




# eval function example with try-except:
while True:
    expression = input("Enter a mathematical expression to evaluate (or 'exit' to quit): ")
    if expression.lower() == 'exit':
        print("Exiting the program.")
        break
    try:
        result = eval(expression)
        # break     ---  doing this will exit the loop on first valid expression making else case useless
    except ValueError:
        print(f'Please enter a vaild number!')
    else:
        print(f'{result}')