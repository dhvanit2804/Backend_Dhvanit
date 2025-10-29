class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent Class Constructor Called")

    def show(self):
        print(f"Parent Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"Child Class Constructor Called")

    def show(self):
        super().show()
        print(f"Child Age: {self.age}")

c = Child("Dhvanit", 21)
c.show()