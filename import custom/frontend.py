import backend as me       # Importing the backend file as alias me

# num = []
# print(me.mean(num))


print("Choose the operation you want to perform:\n1. Arithmetic Operation\n2. Statistical Operation\n")
choice = int(input("Enter the number of operation: "))

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid Input!\nPlease enter valid numbers.\n")

opt = input("Enter the operation you want to perform\nExample: (add for '+',   sub for '-',   mul for 'x',   div for '/'): ").lower()

val = me.calculator(num1, num2, opt)
print(val)