class Parent:
    def parent_info(self):
        print("This is Parent Class")

class Child1(Parent):
    def child1_info(self):
        print("This is Child1 Class")

class Child2(Parent):
    def child2_info(self):
        print("This is Child2 class")

c1 = Child1()
c2 = Child2()

c1.parent_info()
c1.child1_info()

c2.parent_info()
c2.child2_info()