def mean(num):
    return sum(num)/len(num) if num else 0

def calculator(num1, num2, opt):
    if opt == "add":
        return num1 + num2
    elif opt == "sub":
        return num1 - num2
    elif opt == "mul":
        return num1 * num2
    elif opt == "div":
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid Operation!"
    