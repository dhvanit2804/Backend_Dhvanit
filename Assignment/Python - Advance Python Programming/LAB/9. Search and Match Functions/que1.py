'Write a Python program to search for a word in a string using re.search().'

import re

text = "Python is a powerful programming language."

word = "powerful"

result = re.search(word, text)

if result:
    print(f"Word '{word}' found at position {result.start()}")
else:
    print(f"Word '{word}' not found in the string.")