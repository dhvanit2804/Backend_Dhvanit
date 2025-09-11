#include<iostream>
using namespace std;

class Teacher {
public:
	string subject;
	float salary;
};

class Researcher {
public:
	string researchArea;
	int publications;
};

class Professor : public Teacher, public Researcher {
public:
	void input(){
		cout << "Enter subject: ";
        cin >> subject;
        cout << "Enter salary: ";
        cin >> salary;
        cout << "Enter research area: ";
        cin >> researchArea;
        cout << "Enter publications: ";
        cin >> publications;
	}
	
	void display() {
        cout << "Subject: " << subject << ", Salary: " << salary
             << ", Research Area: " << researchArea
             << ", Publications: " << publications << endl;
    }
};

int main(){
	Professor p;
	p.input();
	p.display();
	return 0;
}
