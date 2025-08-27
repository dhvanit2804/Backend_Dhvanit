#include<iostream.h>
#include<conio.h>

void main()
{
	clrscr();

	char name[50];
	int age;

	cout<<"\nEnter your name: ";
	cin>>name;
	cout<<"\nEnter your age: ";
	cin>>age;

	cout<< "Hello " << name << "! You are " << age << " years old.";
	getch();
}