'Write a Python program to demonstrate string slicing'

text = "PythonProgramming"

print(f"Original String: {text}")

print(f"Sliced String (0-6): {text[:6]}")
print(f"Characters from index 6 to 11: {text[6:12]}")
print(f"Last 6 Characters: {text[-6:]}")
print(f"String with step 2: {text[::2]}")
print(f"Reversed String: {text[::-1]}")