class A:
    def show(self):
        print("Show From A")
class B(A):
    def show(self):
        super().show()
        print("Show From B")
class C(A):
    def show(self):
        super().show()
        print("Show From C")
class D(C, B):
    def show(self):
        super().show()
        print("Show From D")

d1 = D()
d1.show()