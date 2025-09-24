'Take two numbers as input and check which one is larger (use relational operators).'

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f'{num1} is larger than {num2}')
elif num1 < num2:
    print(f'{num2} is larger than {num1}')
else:
    print(f'{num1} is equal to {num2}')