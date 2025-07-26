#include<stdio.h>
#include<conio.h>

void main()
{
	int age;
	clrscr();
	printf("\nEnter Your Age : ");
	scanf("%d",age);
	if(age>=18)
	{
		printf("\nYou Are Eligble to Vote...");
	}
	else
	{
		printf("\nYou Are Not Eligble to Vote...");
	}
	getch();
}