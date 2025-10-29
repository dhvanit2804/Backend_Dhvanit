from abc import ABC, abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(self, r):
        pass

class SBI(RBI):

    def show(self):
        print("Hi, I am SBI")
    def roi(self, r):
        print("Rate Of Interest Given By SBI is: ",r)

class HDFC(RBI):

    def show(self):
        print("Hi, I am HDFC")
    def roi(self, r):
        print("Rate Of Interest Given By HDFC is: ",r)

s = SBI()
s.show()
s.roi(6.2)

h = HDFC()
h.show()
h.roi(7.2)