class Father:
    def father_info(self):
        print("This is Father Class")

class Mother:
    def mother_info(self):
        print("This is Mother Class")

class Child(Father, Mother):
    def child_info(self):
        print("This is Child Class")

c = Child()
c.father_info()
c.mother_info()
c.child_info()