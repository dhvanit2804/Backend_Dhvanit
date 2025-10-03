'Remove digits from string'

s = "hello0world2025"
result = 0
for i in s:
    if not i.isdigit() :
        result += 1
print(result)