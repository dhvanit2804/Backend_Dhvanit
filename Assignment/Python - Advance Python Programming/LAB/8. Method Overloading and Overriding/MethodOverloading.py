'Write Python programs to demonstrate method overloading and method overriding.'

class Calculater:
    def add(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print(f"Sum of three numbers: {a+b+c}")
        elif a is not None and b is not None:
            print(f"Sum of two numbers: {a+b}")
        elif a is not None:
            print(f"Only One argument: {a}")
        else:
            print("No arguments provided")

calc = Calculater()
calc.add()
calc.add(5)
calc.add(5, 10)
calc.add(5, 10, 15)