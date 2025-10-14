def add(a, b):
    print("Addition : ", a + b)

def maxoftwo(a, b):
    if a > b:
        print(f"a is greater: {a}")
    else:
        print(f"b is greater: {b}")

def maxofthree(a, b, c):
    if a > b:
        if a > c:
            print(f"a is greater: {a}")
        else:
            print(f"c is greater: {c}")
    else:
        if b > c:
            print(f"b is greater: {b}")
        else:
            print(f"c is greater: {c}")

def prime(a):
    if a%2 != 0:
        for i in range(3, int(a/2)+1,2):
            if a%i==0:
                print(a," Is Not Prime")
                break
        else:
            print(a," Is prime")
    else:
        print(a," Is Not Prime")

def fibonacci(n):
    a,b =0,1
    print(a,end=" ")
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
        print()