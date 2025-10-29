class Grandfather:
    def grandfather_info(self):
        print("This is Grandfather Class")

class Father(Grandfather):
    def father_info(self):
        print("This is Father Class")

class Child(Father):
    def child_info(self):
        print("This is Child Class")

c = Child()

c.grandfather_info()
c.father_info()
c.child_info()