#include<stdio.h>
#include<conio.h>

long int factorial(int n);

void main()
{
	int num;
	long int fact;
	clrscr();

	printf("\nEnter a number: ");
	scanf("%d",&num);

	fact = factorial(num);
	printf("\nFactorial of %d = %ld", num, fact);
	getch();
}
long int factorial(int n)
{
	long int result = 1;
	int i;

	for(i = 1; i <= n; i++)
	{
		result = result * i;
	}
	return result;
}