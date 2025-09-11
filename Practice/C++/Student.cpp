#include<iostream>
using namespace std;

class Student {
	string name;
	int roll;
	float marks;

public:
	Student(string n, int r, float m){
		name = n;
		roll = r;
		marks = m;
		cout << "Constructor called for " << name << endl;
	}
	
	~Student() {
		cout << "Destructor called for " << name << endl;
	}
	
	void display(){
		cout << "Name: " << name << ", Roll no: " << roll << ", Marks: " << marks << endl;
	}
};

int main(){
	Student s1("Dhvanit",28,88);
	s1.display();
	return 0;
}
