import udf

while True:
    print("*"*40)
    print("1. OddEven")
    print("2. MaxOfTwo")
    print("3. MaxOfThree")
    print("4. Prime")
    print("5. Fibonacci")
    print("6. Exit")
    print("*"*40)

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        n1 = int(input("Enter a number: "))
        udf.oddeven(n1)
        print("*"*40)
    elif choice == 2:
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter a number: "))
        udf.maxoftwo(n1,n2)
    elif choice == 3:
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter a number: "))
        n3 = int(input("Enter a number: "))
        udf.maxofthree(n1,n2,n3)
    elif choice == 4:
        n1 = int(input("Enter a number: "))
        udf.prime(n1)
    elif choice == 5:
        n1 = int(input("Enter a number: "))
        udf.fibonacci(n1)
    elif choice == 6:
        print("Thank You For Using Our Services.")
        break
    else:
        print("Invaliad Choice. Please try again")