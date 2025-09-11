#include <iostream>
using namespace std;

class BankAccount {
private:
    double balance;

public:
    
    BankAccount(double initialBalance) {
        if (initialBalance < 0) 
            balance = 0;
        else 
            balance = initialBalance;
    }

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited: " << amount << endl;
        }
    }

    void withdraw(double amount) {
        if (amount > balance) {
            cout << "Insufficient funds!" << endl;
        } else {
            balance -= amount;
            cout << "Withdrawn: " << amount << endl;
        }
    }

    double getBalance() {
        return balance;
    }
};

int main() {
    BankAccount acc(1000);

    acc.deposit(500);
    acc.withdraw(200);
    cout << "Current Balance: " << acc.getBalance() << endl;

    return 0;
}

