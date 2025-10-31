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