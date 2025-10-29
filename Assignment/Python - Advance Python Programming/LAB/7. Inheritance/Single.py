'Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).'

class Parent:
    def display_parent(self):
        print("This is a Parent Class")

class Child(Parent):
    def display_child(self):
        print("This is Child Class")

c = Child()
c.display_parent()
c.display_child()