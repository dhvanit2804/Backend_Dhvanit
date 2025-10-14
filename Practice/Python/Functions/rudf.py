def showmenu():
    print("\n------ Restaurant Menu ------")
    print("1. Pizza - ₹150")
    print("2. Burger - ₹100")
    print("3. Pasta - ₹120")
    print("4. Coffee - ₹80")
    print("5. Dosa - ₹70")
    print("6. Vadapav - ₹40")
    print("7. Dabeli - ₹40")
    print("8. Puff - ₹60")
    print("9. Exit")
    print("-----------------------------")

def getitem(choice):
    if choice == 1:
        return ("Pizza", 150)
    elif choice == 2:
        return ("Burger", 100)
    elif choice == 3:
        return ("Pasta", 120)
    elif choice == 4:
        return ("Coffee", 80)
    elif choice == 5:
        return("Dosa", 70)
    elif choice == 6:
        return ("Vadapav", 40)
    elif choice == 7:
        return ("Dabeli", 40)
    elif choice == 8:
        return ("Puff", 60)
    else:
        return None

def calculateBill(orderlist):
    total = 0
    print("\n------ Your Order ------")
    for item in orderlist:
        name, price = item
        print(f"{name} - ₹{price}")
        total += price
    print("--------------------------")
    print(f"Total Bill: ₹{total}")