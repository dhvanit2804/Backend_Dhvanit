'In this * example, we will see how to use arbitrary arguments in a function.'
'* in this argument are stored in a tuple.'
'* in this if we give *b and *d it is compulsory to give the *c as well.'
'** in this argument are stored in a dictionary.'

def test(a, b, c, *d):
    print(a)
    print(b)
    print(c)
    print(d)
    print(type(d))
    for i in d:
        print(i)

test(10, 20, 30, 40, 50, 60, 70)

def test1(a, b, c, **d):
    print(a)
    print(b)
    print(c)
    print(d)
    print(type(d))
    for i in d:
        print(i, " : ", d[i])

test1(10, 20, 30, name="John", age=25, city="New York")