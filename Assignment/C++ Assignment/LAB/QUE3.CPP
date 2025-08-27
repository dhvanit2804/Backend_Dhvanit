#include<iostream.h>
#include<conio.h>

int main()
{
	clrscr();

	int length,width,area;

	cout<<"\nEnter length of rectangle: ";
	cin>>length;
	cout<<"\nEnter width of rectangle: ";
	cin>>width;

	area = length * width;
	cout<< "\nArea Of rectangle = "<<area;

	getch();
	return 0;
}