'''Write a Python program to find all numbers between 2000 and 3200 that are divisible by 5 but not
divisible by 7, and store them in a list.'''

l = []

for i in range(2000, 3201):
    if i%5 == 0 and i%7!= 0:
        l.append(i)

print(l)