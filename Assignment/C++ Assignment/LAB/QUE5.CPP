#include<iostream.h>
#include<conio.h>

void main()
{
	clrscr();

	const float PI = 3.1416;

	int a = 10, b = 5;
	float radius = 7.5;
	char grade = 'A';

	int sum = a+b;
	int diff = a - b;
	float area = PI * radius * radius;

	cout<<"Constant PI ="<<PI << "\n";
	cout<<"Integer a = "<< a << ", b = "<< b << "\n";
	cout<<"Sum = "<<sum << ", Difference = " <<diff << "\n";
	cout<<"Radius = "<< radius << ", Area of Circle = "<< area << "\n";
	cout<<"Grade = "<<grade << "\n";

	getch();
}