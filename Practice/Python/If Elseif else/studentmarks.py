rno = int(input("Enter Roll Number: "))
name = input("Enter Name: ")
sub1 = float(input("Enter Marks of sub1: "))
sub2 = float(input("Enter Marks of sub2: "))
sub3 = float(input("Enter Marks of sub3: "))

total = sub1 + sub2 + sub3
percentage = total / 3

print("Roll Number:", rno)
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

print("**************")

if percentage>70:
    print("Distincation")
elif percentage>60:
    print("First Class")
elif percentage>50:
    print("Second Class")
elif percentage>40:
    print("Pass Class")
else:
    print("Fail")