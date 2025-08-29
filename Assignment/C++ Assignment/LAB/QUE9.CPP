#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int number = rand() % 100 + 1;  // Random number between 1 and 100
    int guess;
    int attempts = 0;

    cout << "Guess the number (between 1 and 100): ";

    while (true) {
        cin >> guess;
        attempts++;

        if (guess == number) {
            cout << "Congratulations! You've guessed the number in " << attempts << " attempts." << endl;
            break;
        } else if (guess < number) {
            cout << "Too low! Try again: ";
        } else {
            cout << "Too high! Try again: ";
        }
    }

    return 0;
}
