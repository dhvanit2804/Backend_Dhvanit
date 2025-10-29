'Write a Python program to import the math module and use functions like sqrt(), ceil(), floor().'

import math

num = float(input("Enter a number: "))

square_root = math.sqrt(num)
ceil_value = math.ceil(num)
floor_value = math.floor(num)

print(f"Square root of {num} is: {square_root}")
print(f"Ceiling value of {num} is: {ceil_value}")
print(f"Floor value of {num} is: {floor_value}")
