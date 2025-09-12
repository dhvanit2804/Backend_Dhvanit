#include<iostream>
using namespace std;

class Book {
	string title;
public:
	Book(string t) {
		title = t;
	}
	string getTitle() {
		return title;
	}
};

class Library {
	Book b1, b2;
public:
	Library(Book x, Book y) : b1(x), b2(y) {}
	void showBooks() {
		cout << "Books: " << b1.getTitle() << ", " << b2.getTitle() <<endl;
	}
};

int main() {
	Book bk1("C++ Basics"), bk2("OOP Concepts");
	Library lib(bk1, bk2);
	lib.showBooks();
	return 0;
}
