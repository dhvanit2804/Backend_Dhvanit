#include<stdio.h>
#include<conio.h>

void main()
{
	int number,month;
	clrscr();
	//Even or Odd
	printf("\nEnter Integer : ");
	scanf("%d",&number);
	if(number % 2 == 0)
	{
		printf("\n%d is even",number);
	}
	else
	{
		printf("\n%d is odd",number);
	}
	//Month
	printf("\nEnter a month number (1-12) : ");
	scanf("%d",&month);
	switch(month)
	{
		case 1:
		printf("\nMonth : January");
		break;
		case 2:
		printf("\nMonth : Febuary");
		break;
		case 3:
		printf("\Month : March");
		break;
		case 4:
		printf("\Month : April");
		break;
		case 5:
		printf("\Month : May");
		break;
		case 6:
		printf("\nMonth : June");
		break;
		case 7:
		printf("\nMonth : July");
		break;
		case 8:
		printf("\nMonth : August");
		break;
		case 9:
		printf("\nMonth : Sepetember");
		break;
		case 10:
		printf("\nMonth : October");
		break;
		case 11:
		printf("\nMonth : November");
		break;
		case 12:
		printf("\nMonth : December");
		break;
		default:
		printf("\nInvalid month number!");
	  }
	getch();
}