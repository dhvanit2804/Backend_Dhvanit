'Write a Python program that manipulates and prints strings using various string methods.'

# Program to manipulate and print strings using various string methods

text = "  hello python programming  "

print("Original String:", repr(text))

# Using various string methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Stripped string:", text.strip())           # Removes extra spaces
print("Replaced string:", text.replace("python", "Java"))
print("Count of 'o':", text.count('o'))
print("Starts with 'h':", text.startswith("h"))
print("Ends with 'ing':", text.endswith("ing"))
print("Index of 'python':", text.find("python"))
print("Split into words:", text.split())
print("Joined string:", "-".join(["Learn", "Python", "Easily"]))
