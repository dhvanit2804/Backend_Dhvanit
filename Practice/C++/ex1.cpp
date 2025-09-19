#include<iostream>
using namespace std;

class Student{
private:
	string name;
	int age;
public:
	void setname(string n) {
		name = n;
	}
	string getname() {
		return name;
	}
	void setage(int a) {
		age = a;
	}
	int getage() {
		return age;
	}
};

int main() {
	Student s;
	s.setname("Dhvanit");
	s.setage(20);
	cout << "Name: " << s.getname() << endl;
	cout << "Age: " << s.getage() << endl;
	
	return 0;
}
