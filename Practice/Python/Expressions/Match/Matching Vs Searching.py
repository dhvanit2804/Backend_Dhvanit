import re

print("match function")
print(re.match(r'dog','cat dog cat'))

print("search function")
print(re.search(r'dog','cat dog cat'))