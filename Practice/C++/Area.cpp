#include<iostream>
using namespace std;

class Area {
public:
	float calculate(float r) {
		return 3.14 * r * r;
	}
	
	float calculate(float l, float b) {
		return l * b;
	}
	
	float calculate(float b, float h,int) {
		return 0.5 * b * h;
	}
};

int main() {
    Area a;
    cout << "Circle Area: " << a.calculate(5) << endl;
    cout << "Rectangle Area: " << a.calculate(4, 6) << endl;
    cout << "Triangle Area: " << a.calculate(4, 6, 0) << endl;
    return 0;
}
