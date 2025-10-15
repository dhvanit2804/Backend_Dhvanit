class A:
    def show(self):
        print("Show From A")
class B(A):
    def show(self):
        super().show()
        print("Show From B")
class C(B):
    def show(self):
        super().show()
        print("Show From C")

c1 = C()
c1.show()