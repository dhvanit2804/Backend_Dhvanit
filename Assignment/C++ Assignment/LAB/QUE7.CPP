#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 3;

    // Arithmetic Operators
    cout << "Arithmetic Operators:" << endl;
    cout << "a + b = " << a + b << endl;
    cout << "a - b = " << a - b << endl;
    cout << "a * b = " << a * b << endl;
    cout << "a / b = " << a / b << endl;
    cout << "a % b = " << a % b << endl << endl;

    // Relational Operators
    cout << "Relational Operators:" << endl;
    cout << "(a == b) = " << (a == b) << endl;
    cout << "(a != b) = " << (a != b) << endl;
    cout << "(a > b) = " << (a > b) << endl;
    cout << "(a < b) = " << (a < b) << endl << endl;

    // Logical Operators
    cout << "Logical Operators:" << endl;
    cout << "(a > 5 && b < 5) = " << ((a > 5) && (b < 5)) << endl;
    cout << "(a > 5 || b > 5) = " << ((a > 5) || (b > 5)) << endl;
    cout << "!(a > b) = " << (!(a > b)) << endl << endl;

    // Bitwise Operators
    cout << "Bitwise Operators:" << endl;
    cout << "a & b = " << (a & b) << endl;
    cout << "a | b = " << (a | b) << endl;
    cout << "a ^ b = " << (a ^ b) << endl;
    cout << "a << 1 = " << (a << 1) << endl;
    cout << "a >> 1 = " << (a >> 1) << endl;

    return 0;
}

