#include<stdio.h>
#include<conio.h>
#include<string.h>

void main()
{
	char str[50];
	char rev[50];
	clrscr();

	printf("\nEnter a string: ");
	gets(str);

	strrev(str);
	printf("\nReversed String = %s",str);
	getch();
}