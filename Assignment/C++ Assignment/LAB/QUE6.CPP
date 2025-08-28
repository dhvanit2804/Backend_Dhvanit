#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 2;
    float result;

    result = a / b; 
    cout << "Implicit conversion (a/b) = " << result << endl;

    result = (float)a / b;
    cout << "Explicit conversion (float)a/b = " << result << endl;

    double x = 10.75;
    int y = (int)x;
    cout << "Original double x = " << x << endl;
    cout << "After explicit cast to int y = " << y << endl;

    return 0;
}

