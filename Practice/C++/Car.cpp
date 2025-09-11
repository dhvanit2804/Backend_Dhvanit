#include<iostream>
using namespace std;

class car {
	string brand, model;
	float price;
	
public:
	void input(){
		cout << "Enter Brand: ";
		cin >> brand;
		cout << "Enter Model: ";
		cin >> model;
		cout << "Enter Price: ";
		cin >> price;
	}
	
	void display(){
		cout << "Brand: " << brand << ", Model: " << model << ", Price: " << price << endl;
	}
};

int main(){
	car c[3];
	for (int i=0; i<3; i++){
		cout << "\nEnter details of car " << i + 1 << endl;
		c[i].input();
	}
	cout << "\nCar Details:\n";
	for (int i=0; i<3; i++){
		c[i].display();
	}
	
	return 0;
}
