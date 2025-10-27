marks = {
    "Dhvanit" : 99,
    "Meet": 85,
    "Rohan": 76,
    "list" : [1, 2, 3],
    0 : "Dhvanit"
}

print(marks.items()) # Prints keys and values
print(marks.keys()) # Prints only keys
print(marks.values()) # Prints only values

marks.update({"Dhvanit" : 100, "Jainish" : 88}) # Updates existing key and adds new key-value pair
print(marks)

print(marks.get("Dhvanit"))
print(marks.get("Meet1")) # Prints None
# print(marks["Meet1"]) # Raises KeyError
print(len(marks))