#include<stdio.h>
#include<conio.h>

void main()
{
	int a,b,result,choice;
	clrscr();
	printf("\nEnter A : ");
	scanf("%d",&a);
	printf("\nEnter B : ");
	scanf("%d",&b);

	printf("\n\n1. Addition");
	printf("\n2. Substraction");
	printf("\n3. Multiplication");
	printf("\n4. Divison");
	printf("\n");
	printf("\nSelect Your Choice : ");
	scanf("%d",&choice);

	switch(choice)
	{
		case 1:
		result = a + b;
		printf("\nAddition = %d",result);
		break;

		case 2:
		result = a - b;
		printf("\nSubstraction = %d",result);
		break;

		case 3:
		result = a * b;
		printf("\nMultiplication = %d",result);
		break;

		case 4:
		result = a / b;
		printf("\nDivison = %d",result);
		break;

		default:
		printf("\n Invalid Choice..");
		break;
	}
	getch();
}