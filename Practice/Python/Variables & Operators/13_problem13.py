'Write a program that checks if a number is divisible by both 2 or 5 (use logical or).'

num = int(input("Enter a number: "))
is_divisible = (num % 2 == 0) or (num % 5 == 0)
print(f'Is {num} divisible by 2 or 5? {is_divisible}')
