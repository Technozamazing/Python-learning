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
