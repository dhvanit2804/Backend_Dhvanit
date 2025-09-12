#include<iostream>
using namespace std;

class Person {
public:
	string name;
};

class Student : virtual public Person {
public:
	int roll;
};

class Teacher : virtual public Person {
public:
	string subject;
};

class TA : public Student, public Teacher {
public:
	void display() {
		cout << "Name: " << name << ", Roll: " << roll << ", Subject: " << subject << endl;		
	}
};

int main() {
	TA obj;
	obj.name = "Dhvanit";
	obj.roll = 28;
	obj.subject = "Javascript";
	obj.display();
	return 0;
}
