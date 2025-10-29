class Rectangle:
    def __init__(self, *args):
        if len(args) == 0:
            self.width = 0
            self.height = 0
        elif len(args) == 1:
            self.width = args[0]
            self.height = args[0]
        elif len(args) == 2:
            self.width = args[0]
            self.height = args[1]

    def display(self):
        print(f"Width: {self.width}, Height: {self.height}")

r1 = Rectangle()
r2 = Rectangle(5)
r3 = Rectangle(4, 6)

r1.display()
r2.display()
r3.display()