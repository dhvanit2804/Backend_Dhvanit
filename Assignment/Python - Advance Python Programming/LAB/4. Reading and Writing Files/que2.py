'Write a Python program to write multiple strings into a file. '

file = open("example.txt", "w")

file.write("Hello, This is line 1.\n")
file.write("This is line 2.\n")
file.write("And this is line 3.\n")

print("Data written successfully!")

file.close()