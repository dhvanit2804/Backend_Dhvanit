#include <iostream>
using namespace std;

int globalVar = 10; 

void displayVariables(int localVar) {
    cout << "Local variable: " << localVar << endl;
    cout << "Global variable: " << globalVar << endl;
}

int main() {
    int localVar = 5; 
    displayVariables(localVar);
    return 0;
}
