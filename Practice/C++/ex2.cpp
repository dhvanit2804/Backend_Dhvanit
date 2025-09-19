#include<iostream>
using namespace std;

class Animal {
public:
	void eat() {
		cout << "This Animal eats food" << endl;
	}
};

class Dog : public Animal {
public:
	void bark() {
		cout << "Dog barks: Woof Woof" << endl;
	}
};

int main() {
	Dog d;
	d.eat();
	d.bark();
	
	return 0;
}
