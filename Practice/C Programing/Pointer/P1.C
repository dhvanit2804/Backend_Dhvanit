#include<stdio.h>
#include<conio.h>

void main()
{
	int a = 10;
	int *p;

	clrscr();
	p=&a;

	printf("\nValue of a = %d",a);
	printf("\nAddress of a = %u",&a);
	printf("\nValue using pointer = %d",*p);
	printf("\nAddress stored in pointer = %u",p);

	getch();
}