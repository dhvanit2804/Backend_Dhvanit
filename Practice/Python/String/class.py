class Programmer:
    company = "Google"

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def displayInfo(self):
        print(f"{self.name} works at {self.company} as a {self.position} with a salary of {self.salary}")


programmer1= Programmer('Dhvanit', 25000, "Backend Developer")
programmer1.displayInfo()