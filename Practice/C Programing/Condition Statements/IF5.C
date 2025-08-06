//Leep year
#include<stdio.h>
#include<conio.h>

void main()
{
	int year;
	clrscr();
	printf("\nEnter Year : ");
	scanf("%d",&year);
	if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
		printf("\nLeep year");
	else
		printf("\nNot a leep year");
	getch();
}



