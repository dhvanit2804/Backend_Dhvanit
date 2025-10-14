'Functions with No Arguments & No Return Value'

def printlines():
    print("*"*50)

printlines()
print("Welcome to the user defined functions in Python")
printlines()

'Functions with Arguments & No Return Value'

def add(a, b):
    print("Addition : ", a + b)

printlines()
add(int(input("Enter first number : ")), int(input("Enter second number : ")))
printlines()

'Functions with Arguments & Return Value'

def sub(a, b):
    return a - b

printlines()
print(sub(int(input("Enter first number : ")), int(input("Enter second number : "))))
printlines()