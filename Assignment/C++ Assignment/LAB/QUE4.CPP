#include<iostream.h>
#include<conio.h>

int main()
{
	clrscr();

	int num1, num2, sum;

	cout<<"\nEnter first number: ";
	cin>>num1;
	cout<<"\nEnter second number: ";
	cin>>num2;

	sum = num1 + num2;
	cout<<"\nSum = "<<sum;

	getch();
	return 0;
}