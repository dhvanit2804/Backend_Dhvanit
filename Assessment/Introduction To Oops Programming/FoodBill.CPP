#include<iostream>
using namespace std;

class FoodItem {
public:
	int id;
	string name;
	double price;
	
	FoodItem(int i, string n, double p) {
		id = i;
		name = n;
		price = p;
	}
};

class OrderSystem {
private:
	string customerName;
	double totalBill;
	
public:
	OrderSystem() {
		totalBill = 0.0;
	}
	
	void takeCustomerName() {
		cout << "Enter your Name: ";
		getline(cin, customerName);
		cout << "Welcome, " << customerName << "! Let's order food.\n\n";
	}
	
	void displayMenu(FoodItem menu[], int size) {
		cout << "========== MENU ==========\n";
        for (int i = 0; i < size; i++) {
            cout << menu[i].id << ". " << menu[i].name << " - Rs." << menu[i].price << endl;
        }
        cout << "==========================\n";
	}
	
	void takeOrder(FoodItem menu[], int size) {
		int choice, quantity;
		char moreOrder;
		
		do {
			cout << "\nEnter your choice (food number): ";
			cin >> choice;
			
			bool found = false;
			for (int i=0; i<size; i++){
				if (menu[i].id == choice){
					cout << "Enter quantity for " << menu[i].name << ": ";
					cin >> quantity;
					totalBill += (menu[i].price * quantity);
					cout << quantity << " x " << menu[i].name << " added to your order.\n";
					found = true;
					break;
				}
			}
			
			if (!found) {
				cout << "Invalid choice. Please select from the menu.\n";
			}
			
			cout << "Do you want to order more items? (y/n): ";
			cin >> moreOrder;
		} while (moreOrder == 'y' || moreOrder == 'Y');
	}
	
	void generateBill() {
		cout << "\n========== BILL ==========\n";
        cout << "Customer: " << customerName << endl;
        cout << "Total Bill Amount: Rs." << totalBill << endl;
        cout << "==========================\n";
	}
};

int main() {
	FoodItem menu[] = {
		FoodItem(1, "Pizza", 250),
        FoodItem(2, "Burger", 120),
        FoodItem(3, "Pasta", 150),
        FoodItem(4, "Sandwich", 80),
        FoodItem(5, "Cold Drink", 50)
	};
	
	int menuSize = sizeof(menu) / sizeof(menu[0]);
	
	OrderSystem o;
	
	o.takeCustomerName();
    o.displayMenu(menu, menuSize);
    o.takeOrder(menu, menuSize);
    o.generateBill();
    
    cout << "\nThank you for ordering! Visit Again.\n";
    return 0;
}
