'Write a Python program to merge two lists into one dictionary using a loop.'

keys = ['name', 'age', 'city']
values = ['Dhvanit', 25, 'Ahmedabad']

merged_dict = {}
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]
print(merged_dict)