#include<iostream>
using namespace std;

class Shape {
public:
	virtual void area(){
		cout << "Area of shape\n";
	}
};

class Circle : public Shape {
public:
	void area() override {
		float r;
		cout << "Enter radius: ";
		cin >> r;
		cout << "Area of Circle: " << 3.14 * r * r << endl;
	}
};

class Rectangle : public Shape {
public:
	void area() override {
		float l, b;
		cout << "Enter length & breadth: ";
		cin >> l >> b;
		cout << "Area of Rectangle: " << l * b << endl;
	}
};

int main(){
	Shape* s;
	Circle c;
	Rectangle r;
	
	s = &c;
    s->area();

    s = &r;
    s->area();
    
    return 0;
}
