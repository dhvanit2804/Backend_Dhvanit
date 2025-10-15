class Tops:

    def admission(self, moblile, name, course, fees):
        self.moblile = moblile
        self.name = name
        self.course = course
        self.fees = fees
        self.first_paid = False
        self.second_paid = False
        self.third_paid = False
        print("Admission done successfully")
        
    
    def first_installment(self, amount):
        if self.first_paid:
            print("First installment already paid")
        elif amount <= self.fees and amount>0:
            self.fees -= amount
            self.first_paid = True
            print("First installment Succesully deposite")
        else:
            print("Invalid amount entered.")

    def second_installment(self, amount):
        if self.second_paid:
            print("Second installment already paid.")
        elif amount <= self.fees and amount>0:
            self.fees -= amount
            self.second_paid = True
            print("second installment Succesully deposite")
        else:
            print("Invalid amount entered.")
    
    def third_installment(self, amount):
        if self.third_paid:
            print("Third installment already paid.")
        elif amount <= self.fees and amount>0:
            self.fees -= amount
            self.third_paid = True
            print("Third installment Succesully deposite")
        else:
            print("Invalid amount entered.")
    
    def checkDetails(self):
        print("Student details are:")
        print(f"Mobile: {self.moblile}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Pending fees: {self.fees}")

s1 = Tops()
s1.admission(9265920139,"Dhvanit","Backend Development",60000)

while True:
    print("1. First Installment")
    print("2. Second Installment")
    print("3. Third Installment")
    print("4. Check Details")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter the amount for first installment: "))
        s1.first_installment(amount)
    elif choice == 2:
        amount = int(input("Enter the amount for Second installment: "))
        s1.second_installment(amount)
    elif choice == 3:
        amount = int(input("Enter the amount for Third installment: "))
        s1.third_installment(amount)
    elif choice == 4:
        s1.checkDetails()
    elif choice == 5:
        print("Thank you for visiting us.")
        break
    else:
        print("Invalid Choice")
    
    print("*"*50)