#include<iostream>
#include<string>
using namespace std;

int main() {
	string str;
	cout << "Enter a string: ";
	cin >> str;
	
	bool isPalindrome = true;
	int n = str.length();
	
	for (int i=0; i<n/2; i++) {
		if(str[i] != str[n - i -1]) {
			isPalindrome = false;
			break;
		}
	}
	
	if (isPalindrome)
		cout << str << " is a Palindrome." << endl;
	else
		cout << str << " is Not a Palindrome." << endl;
	
	return 0;
}
