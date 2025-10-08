class Employee:
    a = 10
    @classmethod
    def show(cls):
        print(f"The Class value of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

b = Employee()
b.a = 20
b.name = "Dhvanit Parate"
print(b.name)
print(b.fname)
print(b.lname)