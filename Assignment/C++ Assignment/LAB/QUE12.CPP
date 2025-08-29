#include <iostream>
using namespace std;

void add(int a, int b) {
    cout << "Sum: " << a + b << endl;
}

void subtract(int a, int b) {
    cout << "Difference: " << a - b << endl;
}

void multiply(int a, int b) {
    cout << "Product: " << a * b << endl;
}

void divide(int a, int b) {
    if (b != 0)
        cout << "Quotient: " << a / b << endl;
    else
        cout << "Division by zero error!" << endl;
}

int main() {
    int choice, num1, num2;

    cout << "Select operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n";
    cin >> choice;

    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    switch (choice) {
        case 1:
            add(num1, num2);
            break;
        case 2:
            subtract(num1, num2);
            break;
        case 3:
            multiply(num1, num2);
            break;
        case 4:
            divide(num1, num2);
            break;
        default:
            cout << "Invalid choice!" << endl;
    }

    return 0;
}
