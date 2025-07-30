#include<stdio.h>
#include<conio.h>

void main()
{
	int marks;
	char grade,Name[50];
	clrscr();
	printf("\nHello Welcome To Our Result Website\n");

	printf("\nEnter A Student Name : ");
	gets(Name);

	printf("\nEnter a marks : ");
	scanf("%d",&marks);
	if(marks>=90)
	{
		printf("\nGrade A");
	}
	else if(marks>=75)
	{
		printf("\nGrade B");
	}
	else if(marks>=50)
	{
		printf("\nGrade C");
	}
	else if(marks>=40)
	{
		printf("\Grade D");
	}
	else
	{
		printf("\nPass");
	}
	getch();
}