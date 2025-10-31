'Write a Python program to match a word in a string using re.match().'

import re

text = "Python is fun to learn."

word = "Python"

result = re.match(word, text)

if result:
    print(f"String starts with the word '{word}'.")
else:
    print(f"String does not start with the word '{word}'.")