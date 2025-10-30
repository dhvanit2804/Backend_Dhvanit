'Write a Python program to demonstrate handling multiple exceptions.'

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print(f"Result: {result}")

    my_list = [1, 2, 3]
    index = int(input("Enter index to access (0-2): "))
    print(f"Element at index {index} is {my_list[index]}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter integers only.")
except IndexError:
    print("Error: Index out of range.")
except Exception as e:
    print("An unexpected error occurred:", e)