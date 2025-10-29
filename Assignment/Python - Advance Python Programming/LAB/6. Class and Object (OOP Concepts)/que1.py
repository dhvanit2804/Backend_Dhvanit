'Write a Python program to create a class and access its properties using an object.'

class Calculater:

    def add(self, x, y):
        self.x = x
        self.y = y
        return x + y
    def sub(self, x, y):
        self.x = x
        self.y = y
        return x - y

c = Calculater()
print(c.add(10, 20))
print(c.sub(10, 5))