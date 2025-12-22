# Recursion:
# When a function calls itself repeatedly.
# Note: For a recursive function - base case is very needed 

# Recursion is like the advance version of loop
# Anything which can be done through loop can be done through recursion
# and vice-versa


# WARF to print from n to 1 backward:
def show(n):
#               ----------------- 

    if n == 0:    # Base Case
        return
#               ------------------
    print(n)      # function body
#               ------------------    
    show(n-1)     # recursion_call
#               ------------------


# Note: Base Case is like the terminating condition in loop 
# not defining condition will make the loop run infinitly 
# Similar to that - not defining base case will make the recursive function to run infinitly



# WARF to find the factorial of a given number:
def factorial(num):
    if num == 1:
        fac = 1
        return fac
    else:
        return num * factorial(num - 1)

print(f'Factorial of the given number is {factorial(4)}')



# Problems to solve:
# Write a recursive function to calculate the sum of first n naturral numbers.
# Write a recursive function to print all elements in a list. (Hint: use list or index as parameters)
pass   # future more practice in recursion is needed.