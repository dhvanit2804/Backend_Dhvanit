class Bank:
    def getroi(self):
        return 10
    
class SBI(Bank):
    def getroi(self):
        return 7
    
class ICICI(Bank):
    def getroi(self):
        return 8

b1 = Bank()
b2 = SBI()
b3 = ICICI()

print(f"Bank Rate Of Interest: {b1.getroi()}")
print(f"SBI Rate Of Interest: {b2.getroi()}")
print(f"ICICI Rate Of Interest: {b3.getroi()}")