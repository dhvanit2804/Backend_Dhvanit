session = {
    "logged in": False,
    "email": ""
}

valid_email = "dhvanitparate123@gmail.com"
valid_password = "dhvanit123"

def login_required(func):
    def wrapper():
        if session['logged in']:
            func()
        else:
            print("Access Denied! Please Login First.\n")
    return wrapper

def login():
    email = input("Enter Email Address: ")
    password = input("Enter Password: ")

    if email == valid_email and password == valid_password:
        session['logged in'] = True
        session['email'] = email
        print("\nLogin Successfull!\n")
    else:
        print("\nInvalid Email Or Password\n")


@login_required
def profile():
    print(f"Welcome, {session['email']}! This is your profile.\n")

@login_required
def account():
    print("Here is your account information.\n")

def logout():
    session['logged in'] = False
    session['email'] = ""
    print("You have been logged out.\n")

def main():
    while True:
        print("=== Menu ===")
        print("1. Login")
        print("2. Profile")
        print("3. Account")
        print("4. Logout")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            profile()
        elif choice == "3":
            account()
        elif choice == "4":
            logout()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice. Try Again.\n")

main()