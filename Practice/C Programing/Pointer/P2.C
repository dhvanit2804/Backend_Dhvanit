#include<stdio.h>
#include<conio.h>

void swap(int *x, int *y)
{
	int temp;
	temp = *x;
	*x = *y;
	*y = temp;
}

void main()
{
	int a = 5, b=10;
	clrscr();

	printf("\nBefore Swap: a=%d b=%d", a,b);
	swap(&a,&b);
	printf("\nAfter Swap: a=%d b=%d",a,b);

	getch();
}