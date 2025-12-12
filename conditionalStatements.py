# Grade Calculator
name = input('Enter name of student: ')
sub1 = float(input('Enter marks of subject 1: '))
sub2 = float(input('Enter marks of subject 2: '))
sub3 = float(input('Enter marks of subject 3: '))
total = sub1 + sub2 + sub3
percentile = (total / 300)*100

if percentile >= 90:
    grade = 'A+'
elif percentile >= 80 and percentile < 90:
    grade = 'A'
elif percentile >= 70 and percentile < 80:
    grade = 'B+'
elif percentile >= 60 and percentile < 70:
    grade = 'B'
elif percentile >= 50 and percentile < 60:
    grade = 'C+'
elif percentile >= 40 and percentile < 50:
    grade = 'C'
elif percentile >= 30 and percentile < 40:
    grade = 'D'
else:
    grade = 'F'

print(f'\nStudent Name: {name}')
print(f'Total Marks: {total} out of 300')
print(f'Percentage: {percentile:.2f}%')



# Simple Even or Odd Checker
num = int(input('Enter a Number:'))
print(f'Entered number {num} is even') if num %2 == 0 else print(f'Entered number {num} is odd')  # Ternary Conditional Operator  
                                                                                                  # <true_expression> if <condition> else <false_expression>



# Voter Qualification Checker
age = int(input('Enter age of voter: '))
print('\nYou are eligible to vote.') if age >= 18 else print('\nYou are not eligible to vote.')


# Traffic Light Simulation
light = input('Enter traffic light color (red, yellow, green):').lower()
if light == 'red':
    print('Stop!')
elif light == 'yellow':
    print('Get Ready!')
elif light == 'green':
    print('Go!')
else:
    print('Invalid color!')


# Salary Taxation Calculator
# Logic: for annual salary upto 50,000 10% tax, for salary greater than 50,000 20% tax
# Clever way using ternary operator (false_value, true_value) [condition]
salary = float(input('Enter Annual Salary: '))
#tax = (salary * 0.10) if salary <= 50000 else (salary * 0.20)
tax = salary *(0.2, 0.1)[salary <= 50000] # Using tuple indexing for conditional selection

print(f'\nFor an annual salary of {salary}, the tax to be paid is: {tax}')



# Greatest of Three Numbers
print(f'Enter three numbers for comparison')
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
num3 = float(input('Enter the third number: '))

if num1 >= num2 and num1 >= num3:
    print(f'Greatest among the three is "{num1}"')
elif num2 >= num1 and num2 >= num3:
    print(f'Greatest among the three is "{num2}"')
elif num3 >= num1 and num3 >= num2:
    print(f'Greatest among the three is "{num3}"')
else:
    print('All three numbers are equal.')



# Improved version
def are_all_equal(a, b, c):
    """
    Checks if all three numbers are equal, which is the condition 
    where none of the numbers are strictly greater than the others.
    """
    if a == b and b == c:
        return True
    else:
        return False

# --- Test Cases ---

# Case 1: All numbers are the same
num1_a = 5.5
num1_b = 5.5
num1_c = 5.5
result1 = are_all_equal(num1_a, num1_b, num1_c)
print(f"Are {num1_a}, {num1_b}, {num1_c} all equal? {result1}")
# Expected output: True


# Case 2: Numbers are different
num2_a = 10
num2_b = 20
num2_c = 10
result2 = are_all_equal(num2_a, num2_b, num2_c)
print(f"Are {num2_a}, {num2_b}, {num2_c} all equal? {result2}")
# Expected output: False


# Case 3: Two numbers are equal, one is different (e.g., the largest case)
num3_a = 10
num3_b = 10
num3_c = 15
result3 = are_all_equal(num3_a, num3_b, num3_c)
print(f"Are {num3_a}, {num3_b}, {num3_c} all equal? {result3}")
# Expected output: False