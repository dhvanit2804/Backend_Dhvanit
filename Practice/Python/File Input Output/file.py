file = open("tops.txt","w") # w for write
file.write("Welcome to the file management learning in a python")
file.close()
print("File Written Succesfully")
print("*****************************************************")

file = open("tops.txt","r") # r for read
print(file.read())
file.close()
print("*****************************************************")

file = open("tops.txt","a") # a for append
file.write("\nFile Management With Python Is Very Easy To Learn.")
file.close()
print("*****************************************************")

file = open("tops.txt","r")
print(file.read())
file.close()
print("*****************************************************")

file = open("tops1.txt","w+") # w+ for write and read
file.write("This is w+ operation in python.")
print("File Current Position : ",file.tell())
file.seek(0)
print("File Data :",file.read())
file.close()