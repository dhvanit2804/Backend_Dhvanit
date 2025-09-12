#include<iostream>
using namespace std;

class Printable {
public:
	virtual void print() = 0;
};

class Student : public Printable {
public:
	void print() {
		cout << "Printing Student Details" << endl;
	}
};

class Teacher : public Printable {
public:
	void print() {
		cout << "Printing Teacher Details" << endl;
	}
};

int main() {
	Printable* p;
	Student s;
	Teacher t;
	
	p = &s; p->print();
    p = &t; p->print();
    
    return 0;
}
