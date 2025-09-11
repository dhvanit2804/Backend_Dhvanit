#include<iostream>
using namespace std;

class Person {
public:
	string name;
	int age;
	
	void inputdetails(string n, int a){
		name = n;
		age = a;
	}
	
	void displaydetails(){
		cout << "Name: " << name << ", Age: " << age << endl;
	}
};

class Student : public Person {
public:
	string course;
	
	void setStudent(string n, int a, string c){
		inputdetails(n,a);
		course = c;
	}
	
	void showStudent(){
		displaydetails();
		cout << "Course: " << course << endl;
	}
};

class Teacher : public Person {
public:
	string subject;
	
	void setTeacher(string n, int a, string s) {
		inputdetails(n,a);
		subject = s;
	}
	
	void showTeacher() {
		displaydetails();
		cout << "Subject: " << subject << endl;
	}
};

int main() {
	Student s;
	s.setStudent("Dhvanit", 21, "Computer Science");
    cout << "Student Details:" << endl;
    s.showStudent();

    Teacher t;
    t.setTeacher("Mr. Sharma", 40, "Mathematics");
    cout << "\nTeacher Details:" << endl;
    t.showTeacher();

    return 0;
}
