#include<iostream>
using namespace std;

class Box {
	float length, width, heigth;
	
public:
	Box(float l, float w, float h){
		length = l;
		width = w;
		heigth = h;
	}
	
	friend float volume(Box b);
};

float volume(Box b) {
	return b.length * b.width * b.heigth;
}

int main() {
	Box b1(2, 3, 4);
	cout << "Volume of box: " << volume(b1) << endl;
	return 0;
}
