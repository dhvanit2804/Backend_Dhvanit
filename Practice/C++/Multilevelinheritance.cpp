#include<iostream>
using namespace std;

class Person {
public:
	string name;
	int age;
};

class Student : public Person {
public:
	string course;
};

class GraduateStudent : public Student {
public:
	float gpa;
	
	void input(){
		cout << "Enter Name: ";
		cin >> name;
		cout << "Enter age: ";
		cin >> age;
		cout << "Enter Course: ";
		cin >> course;
		cout << "Enter GPA: ";
		cin >> gpa;
	}
	
	void display(){
		cout << name << " (" << age << "), Course: " << course << ", GPA: " << gpa << endl;
	}
};

int main(){
	GraduateStudent g;
	g.input();
	g.display();
	return 0;
}
