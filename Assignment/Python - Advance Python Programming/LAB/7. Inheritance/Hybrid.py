class A:
    def display_a(self):
        print("Class A")

class B(A):
    def display_b(self):
        print("Class B")

class C(A):
    def display_c(self):
        print("Class C")

class D(B, C):
    def display_d(self):
        print("Class D")

obj = D()
obj.display_a()
obj.display_b()
obj.display_c()
obj.display_d()
