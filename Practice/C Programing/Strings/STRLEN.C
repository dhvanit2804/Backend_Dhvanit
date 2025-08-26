#include<stdio.h>
#include<conio.h>
#include<string.h>

void main()
{
	char str[100];
	int length;
	clrscr();

	printf("\nEnter a string: ");
	gets(str);

	length = strlen(str);

	printf("\nLength of string = %d",length);
	getch();
}