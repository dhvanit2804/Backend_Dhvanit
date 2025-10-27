class A:
    def show(self):
        print("Show From A")
class B(A):
    def show(self):
        super().show()
        print("Show From B")
class