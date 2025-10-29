'What is Constructor?'
'A constructor is a special method that is automatically called when an object of a class is created.'
'It is used to initialize the attributes of the class.'
'It is defined using the __init__() method.'

class Point:

    def __init__(self,x,y):
        print("init called")
        self.x = x
        self.y = y
    def __str__(self):
        print("str called")
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,obj):
        print("Add Called")
        x = self.x+obj.x
        y = self.y+obj.y
        return Point(x,y)
    def __sub__(self,s):
        print("Sub Called")
        x = self.x - s.x
        y = self.y - s.y
        return Point(x, y)

p1 = Point(10, 20)
print(p1)

p2 = Point(30, 40)
print(p2)

print("Addition Of Objects : ",p1+p2)
print("Substraction Of Objects: ",p1-p2)