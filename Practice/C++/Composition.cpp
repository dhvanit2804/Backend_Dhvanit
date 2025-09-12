#include<iostream>
using namespace std;

class Engine {
public:
	void start(){
		cout << "Engine Started\n";
	}
};

class Car {
	Engine e;
public:
	void drive(){
		e.start();
		cout << "Car is moving\n";
	}
};

int main(){
	Car c;
	c.drive();
	return 0;
}
