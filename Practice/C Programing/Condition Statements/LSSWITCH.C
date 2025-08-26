#include<stdio.h>
#include<conio.h>

void main()
{
	int a,b,c;
	int large,small;
	int lcase,Scase;
	clrscr();
	printf("\nEnter A : ");
	scanf("%d",&a);
	printf("\nEnter B : ");
	scanf("%d",&b);
	printf("\nEnter C : ");
	scanf("%d",&c);
	// Large
	if(a>=b && a>=c)
		lcase = 1;
	else if(b>=a && b>=c)
		lcase = 2;
	else
		lcase = 3;

	switch(lcase){
		case 1:
		large = a;
		break;
		case 2:
		large = b;
		break;
		case 3:
		large = c;
		break;
	}
	// Small
	if(a<=b && a<=c)
		Scase = 1;
	else if(b<=a && b<=c)
		Scase = 2;
	else
		Scase = 3;

	switch(Scase){
		case 1:
		small = a;
		break;
		case 2:
		small = b;
		break;
		case 3:
		small = c;
		break;
	}
	printf("\nLargest Num = %d\n",large);
	printf("\nSmallest Num = %d",small);
	getch();
}