//Largest Number amoung 3
#include<stdio.h>
#include<conio.h>

void main()
{
	int a,b,c;
	clrscr();
	printf("\nEnter A : ");
	scanf("%d",&a);
	printf("\nEnter B : ");
	scanf("%d",&b);
	printf("\nEnter C : ");
	scanf("%d",&c);
	if(a>=b && a>=c)
		printf("\nLargest is = %d",a);
	else if(b>=a && b>=c)
		printf("\nLargest is = %d",b);
	else
		printf("\nLargest is = %d",c);
	getch();
}
