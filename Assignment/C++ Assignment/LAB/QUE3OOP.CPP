#include<iostream.h>
#include<conio.h>

class Rectangle
{
	int length, width;
public:
	void input()
	{
		cout<<"\nEnter length of rectangle: ";
		cin>>length;
		cout<<"\nEnter Width of rectangle: ";
		cin>>width;
	}
	int area()
	{
		return length * width;
	}
};

int main()
{
	clrscr();

	Rectangle r;
	r.input();
	cout<<"\nArea of rectangle = "<<r.area();
	getch();
	return 0;
}