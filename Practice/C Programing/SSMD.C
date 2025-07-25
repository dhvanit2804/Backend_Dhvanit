#include<stdio.h>
#include<conio.h>

void main()
{
	int a,b;
	clrscr();
	printf("\nEnter A Number : ");
	scanf("%d",&a);
	printf("\nEnter B Number : ");
	scanf("%d",&b);
	printf("\nSum = %d", a + b);
	printf("\nSub = %d", a - b);
	printf("\nMul = %d", a * b);
	printf("\nDiv = %d", a / b);
	getch();
}