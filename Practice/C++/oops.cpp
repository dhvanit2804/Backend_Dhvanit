#include<iostream>
using namespace std;

class Car {
private:
	string brand;
	int year;
	
public:
	Car(string b, int y) {
		brand = b;
		year = y;
	}
	
	void setBrand(string b) {
		brand = b;
	}
	
	string getBrand() {
		return brand;
	}
	
	void setYear(int y) {
		year = y;
	}
	
	int getYear() {
		return year;
	}
	
	virtual void displayInfo() = 0;
	virtual void mileage() = 0;
};

class ElectricCar : public Car {
private:
	int batteryLife;
	
public:
	ElectricCar(string b, int y, int battery) : Car(b, y) {
		batteryLife = battery;
	}
	
	void displayInfo() override {
        cout << "Electric Car: " << getBrand() << " (" << getYear() << ")"
             << " | Battery Life: " << batteryLife << " hrs" << endl;
    }

    void mileage() override {
        cout << "Mileage: 6 km per 1% battery" << endl;
    }
};

class PetrolCar : public Car {
private:
	int fuelTank;
public:
	PetrolCar(string b, int y, int tank) : Car(b, y) {
		fuelTank = tank;
	}
	
	void displayInfo() override {
        cout << "Petrol Car: " << getBrand() << " (" << getYear() << ")"
             << " | Fuel Tank: " << fuelTank << " liters" << endl;
    }
    
    void mileage() override {
		cout << "Mileage: 15 km per liter" << endl;
	}
};

int main() {
	Car* c1 = new ElectricCar("Tesla", 2023, 24);
	Car* c2 = new PetrolCar("Toyota", 2022, 45);
	
	c1->displayInfo();
	c1->mileage();
	
	cout << endl;
	
	c2->displayInfo();
	c2->mileage();
	
	delete c1;
	delete c2;
	
	return 0;
}
