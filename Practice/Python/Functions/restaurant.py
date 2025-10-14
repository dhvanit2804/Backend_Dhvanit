import rudf

orderlist = []

while True:
    rudf.showmenu()
    choice = int(input("Enter your choice: "))

    if choice in [1, 2, 3, 4, 5, 6, 7, 8]:
        item = rudf.getitem(choice)
        orderlist.append(item)
        print(f"{item[0]} added to your order.")
        print("*"*40)
    elif choice == 9:
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice. Please try again.")
        print("*" * 40)

if len(orderlist) > 0:
    rudf.calculateBill(orderlist)
else:
    print("No items orderd.")