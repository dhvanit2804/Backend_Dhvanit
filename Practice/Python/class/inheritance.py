class A:

    def getA(self, a):
        self.a = a
    def putA(self):
        print(f"A : {self.a}")

class B(A):

    def getB(self, b):
        self.b = b
    def putB(self):
        print(f"B : {self.b}")

class C(A):

    def getC(self, c):
        self.c = c
    def putC(self):
        print(f"C : {self.c}")

class D(B, C):

    def getD(self, d):
        self.d = d
    def putD(self):
        print(f"D : {self.d}")

d1 = D()
d1.getA(10)
d1.getB(20)
d1.getC(30)
d1.getD(40)
d1.putA()
d1.putB()