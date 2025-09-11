#include<iostream>
using namespace std;

class Person {
public:
	string name;
	int age;
};

class Employee : public Person {
public:
	float salary;
	string designation;
	
	void input(){
		cout << "Enter Name: ";
		cin >> name;
		cout << "Enter age: ";
		cin >> age;
		cout << "Enter Salary: ";
		cin >> salary;
		cout << "Enter designation: ";
		cin >> designation;
	}
	
	void display(){
		cout << name << " (" << age << ") - " << designation << " - Salary: " << salary << endl;
	}
};

int main(){
	Employee e1;
	e1.input();
	e1.display();
	return 0;
}
