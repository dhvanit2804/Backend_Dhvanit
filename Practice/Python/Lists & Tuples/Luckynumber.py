import random

# print(random.randint(1000,9999))
# print(random.choice([1, 2, 3, "java", "react", "javascript", 1.1, 22]))

l = []
lucky = []

for i in range(1, 101):
    l.append(i)

for i in range(10):
    num = random.choice(l)
    lucky.append(num)
    l.remove(num)

print(l)
print(lucky)