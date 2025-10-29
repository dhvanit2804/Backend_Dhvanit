' 12) Write a Python program to demonstrate the use of local and global variables in a class.'

# Global variable
num = 100

class Demo:
    def show(self):
        # Local variable
        num = 50
        print("Local variable inside method:", num)
        # Accessing global variable using globals() function
        print("Global variable inside method:", globals()['num'])

# Create object of the class
d = Demo()
d.show()

print("Global variable outside class:", num)
