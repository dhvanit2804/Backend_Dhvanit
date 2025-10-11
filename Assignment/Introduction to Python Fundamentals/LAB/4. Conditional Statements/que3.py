'''Practical Example 7: Write a Python program to calculate grades based on percentage using 
if-else ladder. '''

sname = input("Enter a student name: ")
rno = int(input("Enter a roll number: "))
sub1 = float(input("Enter a Marks of sub1: "))
sub2 = float(input("Enter a Marks of sub2: "))
sub3 = float(input("Enter a Marks of sub3: "))

total = sub1 + sub2 + sub3
percentage = total/3

print("Name:",sname)
print("Roll Number:", rno)
print("Total:",total)
print("Percentage:",percentage)

print("***************")

if percentage > 70:
    print("Distincation")
elif percentage > 60:
    print("First Class")
elif percentage > 50:
    print("Second Class")
elif percentage > 40:
    print("Pass Class")
else:
    print("Fail")