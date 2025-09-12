#include<iostream>
using namespace std;

class B;

class A {
	int x;
public:
	A(int val) {
		x = val;
	}
	friend class B;
};

class B {
public:
	void show(A & obj) {
		cout << "Value of x: " << obj.x << endl;
	}
};

int main() {
	A a1(10);
	B b1;
	b1.show(a1);
	return 0;
}
