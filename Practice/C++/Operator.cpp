#include<iostream>
using namespace std;

class Complex {
	int real, imag;
	
public:
	Complex(int r = 0, int i = 0){
		real = r;
		imag = i;
	}
	
	Complex operator+(Complex c){
		return Complex(real + c.real, imag + c.imag);
	}
	
	bool operator==(Complex c){
		return (real == c.real && imag == c.imag);
	}
	
	void display() {
		cout << real << " + " << imag << "i" << endl;
	}
};

int main(){
	Complex c1(3, 4), c2(1, 2);
	Complex c3 = c1 + c2;
	cout << "Sum: ";
	c3.display();
	
	if (c1 == c2)
		cout << "Complex numbers are equal\n";
	else
		cout << "Complex numbers are not equal\n";
	
	return 0;
}
