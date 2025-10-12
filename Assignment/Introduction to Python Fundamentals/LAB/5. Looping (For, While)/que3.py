'''Practical Example 3: Write a Python program to find a specific string in the list using a simple 
for loop and if condition.'''

List1 = ['apple', 'banana', 'mango']
search = 'mango'

for fruit in List1:
    if fruit == search:
        print(f"'{search}' found in the list!")
        break
else:
    print(f"'{search}' is not found in the list.")