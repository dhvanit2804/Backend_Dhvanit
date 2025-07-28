#include<stdio.h>
#include<conio.h>

void main()
{
	int a,b,result;
	char operater;
	clrscr();
	printf("\nEnter A : ");
	scanf("%d",&a);
	printf("\nEnter a operator (+,-,*,/) : ");
	fflush(stdin);
	scanf("%c",&operater);
	printf("\nEnter B : ");
	scanf("%d",&b);

	if(operater == '+')
	{
		result = a + b;
		printf("\nResult = %d",result);
	}
	else if(operater == '-')
	{
		result = a - b;
		printf("\nResult = %d",result);
	}
	else if(operater == '*')
	{
		result = a * b;
		printf("\nResult = %d",result);
	}
	else if(operater == '/')
	{
		if(b !=0){
			result = a / b;
			printf("\nResult = %d",result);
		}
		else
		{
			printf("\nError : Divison by Zero Not Valid..");
		}
	}
	else
	{
		printf("\nInvalid Operater");
	}
	getch();
}