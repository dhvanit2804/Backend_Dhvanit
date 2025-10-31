from datetime import datetime

rentals = []
LATE_FEE_PER_DAY = 10

def rent_book():
    print("\n--- Book Rental Booking ---")
    customer = input("Enter Customer Name: ")
    book = input("Enter book title: ")
    rental_date = input("Enter rental date (YYYY-MM-DD): ")
    due_date = input("Enter expected return date (YYYY-MM-DD): ")

    rental = {
        "customer" : customer,
        "book": book,
        "rental_date": rental_date,
        "due_date": due_date,
        "returned": False
    }

    rentals.append(rental)
    print(f"\n Book '{book}' rented successfully to {customer}.\n")

def return_book():
    print("\n--- Book Return ---")
    book_title = input("Enter book title to return: ")
    return_date = input("Enter actual return date (YYYY-MM-DD): ")

    for rental in rentals:
        if rental["book"].lower() == book_title.lower() and not rental["returned"]:
            rental["returned"] = True


            due = datetime.strptime(rental["due_date"], "%Y-%m-%d")
            actual = datetime.strptime(return_date, "%Y-%m-%d")
            delay = (actual - due).days

            late_fee = LATE_FEE_PER_DAY * delay if delay > 0 else 0

            print("\n----- RENTAL RECEIPT -----")
            print(f"Customer Name : {rental['customer']}")
            print(f"Book Title    : {rental['book']}")
            print(f"Rented On     : {rental['rental_date']}")
            print(f"Due Date      : {rental['due_date']}")
            print(f"Returned On   : {return_date}")
            print(f"Late Days     : {delay if delay > 0 else 0}")
            print(f"Late Fee      : ₹{late_fee}")
            print("---------------------------\n")
            return
    
    print("❌ Book not found or already returned.\n")


def show_summary():
    print("\n--- Current Rentals Summary ---")
    if not rentals:
        print("No rentals recorded yet.\n")
        return
    
    for r in rentals:
        status = "Returned" if r["returned"] else "Rented"
        print(f"{r['customer']} | {r['book']} | {r['rental_date']} to {r['due_date']} | {status}")
    print()

def main():
    while True:
        print("====== RentTrack Library System ======")
        print("1. Book Rental Booking")
        print("2. Book Return & Late Fee Calculation")
        print("3. View Rental Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            rent_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Thank you for using Service!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()