#include<iostream.h>
#include<conio.h>

class Student
{
	int rno;
	char *sname;
	public:
	void getdata()
	{
		cout<<"\nEnter Roll No : ";
		cin>>rno;
		cout<<"\nEnter Student Name : ";
		cin>>sname;
	}
	void putdata();
};
void Student::putdata()
{
	cout<<"\nRoll No : "<<rno;
	cout<<"\nStudent Name : "<<sname;
}
void main()
{
	Student s1;
	clrscr();
	s1.getdata();
	s1.putdata();
	getch();
}