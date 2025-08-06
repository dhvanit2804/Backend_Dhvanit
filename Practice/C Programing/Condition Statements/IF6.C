#include<stdio.h>
#include<conio.h>

void main()
{
	int a,b,result,choice;
	clrscr();
	printf("\n1. Addition\n2. Substraction\n3. Mutliplication\n4. divison");
	printf("\n\nEnter Your Choice : ");
	scanf("%d",&choice);
	printf("\nEnter A : ");
	scanf("%d",&a);
	printf("\nEnter B : ");
	scanf("%d",&b);
	switch(choice){
		case 1:
		result = a + b;
		printf("\nResult = %d",result);
		break;
		case 2:
		result = a - b;
		printf("\nResult = %d",result);
		break;
		case 3:
		result = a * b;
		printf("\nResult = %d",result);
		break;
		case 4:
		if(b!=0){
			result = a / b;
			printf("\nResult = %d",result);
		}
		else{
			printf("Not divison by Zero");
		}
		break;
	}
	getch();
}