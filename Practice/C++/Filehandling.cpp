#include<iostream>
#include<fstream>
using namespace std;

class Student {
public:
	int roll;
	string name;
	float marks;
	
	void input(){
		cout << "Enter roll, name, marks: ";
		cin >> roll >> name >> marks;
	}
	
	void display(){
		cout << roll << " " << name << " " << marks << endl;
	}
};

int main(){
	ofstream fout("students.txt");
	Student s[2];
	
	cout << "Enter 2 Student details:\n";
	for (int i = 0; i < 2; i++) {
		s[i].input();
		fout << s[i].roll << " " << s[i].name << " " << s[i].marks << endl;
	}
	fout.close();
	
	ifstream fin("students.txt");
	cout << "\nStudent Data from File:\n";
	int r;
	string n;
	float m;
	while (fin >> r >> n >> m) {
		cout << r << " " << n << " " << m << endl;
	}
	fin.close();
	return 0;
}
