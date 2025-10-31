import re
import sys
pattern = 'Fred'
file = open("text.txt","r")

regexp = re.compile(pattern)
for line in file:
    match = regexp.search(line)
    if match:
        print(line)