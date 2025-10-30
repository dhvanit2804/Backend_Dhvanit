'Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).'

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid Operation!")
        result = None

    if result is not None:
        print(f"Result: {result}")

except ValueError:
    print("Error: Invalid number entered. Please enter numeric values only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")