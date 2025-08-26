#include<stdio.h>
#include<conio.h>
#include<string.h>

void main()
{
	char str1[] = "Javascript";
	char str2[50];

	clrscr();
	strcpy(str2, str1);
	printf("Copied String = %s",str2);
	getch();
}