'Find student with highest marks'
students = {"Aman": 85, "Dhvanit": 92, "Riya": 88}

topper = max(students, key=students.get)
print(topper)
print(f"Topper : {topper}, Marks : {students[topper]}")