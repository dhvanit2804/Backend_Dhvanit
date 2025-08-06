//factorial of num
#include<stdio.h>
#include<conio.h>

void main()
{
	int n,i,fact=1;
	clrscr();
	printf("\nEnter N : ");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		fact*=i;
	}
	printf("\nFactorial Of Num = %d",fact);
	getch();
}
