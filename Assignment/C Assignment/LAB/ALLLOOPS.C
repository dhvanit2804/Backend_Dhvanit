#include<stdio.h>
#include<conio.h>

void main()
{
	int i;
	clrscr();
	//for loop
	printf("\nUsing for loop");
	for(i=1;i<=10;i++)
	{
		printf("\n%d",i);
	}
	//while loop
	printf("\nUsing While loop");
	i=1;
	while(i<=10)
	{
		printf("\n%d",i);
		i++;
	}
	//do while loop
	printf("\nUsing Do While Loop");
	i=1;
	do {
		printf("\n%d",i);
		i++;
	}while(i<=10);
	getch();
}