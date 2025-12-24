# This is the beginning of this file
# Its contains all the thing related to Python problems done during Campus Lecture.



# WAP to find the number is +ve, -ve or zero

num = int(input("Enter a Number:"))
if num > 0:
    print(f"Entered number {num} is Positive")
elif num < 0:
    print(f'Entered number {num} is Negative')
else:
    print("Entered number is 0")



# WAP to ask the person age. If they are 18 or older print -- You are adult, else print -- You are minor
age = int(input("Enter age of a person: "))
if age >= 18:
    print('You are an Adult')
elif age <18:
    print('You are a Minor')



# check if the user input username and password is correct or incorrect:

userName = input("Enter Your Username: ")
password = input("Enter Your Password: ")

originalUser = "roman"
originalPass = "roman"

if originalUser == userName and originalPass == password:
    print("Login Successful!")
else:
    print("Invalid Username or Password!")









# Python Lab: 01
# 1. WAP that accepts a student''s name , roll number and marks of three subjects. Calculate the average and print the student details along with the average marks.
name = input(f"Enter Student's Name: ")
sub = ["Maths", "Science", "English"]
rollNumber = input("Enter Student's Roll Number: ")
marks = []

for i in range(3):
    mark = float(input(f"Enter Marks in {sub[i]}: "))
    marks.append(mark)

average = (marks[0] + marks[1] + marks[2]) / 3

print(f"\nStudent Details:")
print(f"Name: {name}")
print(f"Roll Number: {rollNumber}")
print(f"Average Marks: {average}")



# 2. WAP to determine whether a given year is a leap year or not.
year = int(input("Enter a Year: "))
if year % 400 == 0 or year % 4 == 0:
    print(f'Entered year {year} is a Leap year.')
else: 
    print(f"Entered year {year} is not a Leap year.")



# 3. WAP that takes a number as input. If the number is divisible by 2,3 and 5 at the same time, print "Super Divisible", else  print which of the number it is divisible by.
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print(f'Nmber {num} is Super Divisible.')
else:
    print(f'Number {num} is not Super Divisible.')
    # for i in range
    num = 1
    test = num % 2 == 0 and num % 3 == 0 and num % 5 == 0
    while not test:
        num += 1
        test = num % 2 == 0 and num % 3 == 0 and num % 5 == 0
    print(f'Next Super Divisible number is {num}')



# 4. Develop a Python program to print numbers from 1 to 50.
#    The program should skip all the numbers that are divisible by 5 using the continue statement.
for i in range(1, 51, 1):
    if i % 5 != 0:
        print(i)



# 5. WAP to takes numbers continuously from the user until the user enters 0. For each  number entered, displey wheather it is even or odd.
while True:
   num = int(input(f'Enter a number: (Zero to exit.)'))
   if num == 0:
       print('You have entered Zero.')
       break
   elif num % 2 == 0:
       print(f"{num} is even.")
   else:
       print(f"{num} is odd.")



# 6. WAP to repaetly ask user to enter a password until the correct password is entered. 
# Print "Access Granted" when the correct password is entered.
correct_password = "admin123"
while True:
    password = input("Enter a password: ")
    if correct_password == password:
        print("Access Granted!")
        break
    else:
        print("Incorrect Password!\nTry Again!")



# 7. 