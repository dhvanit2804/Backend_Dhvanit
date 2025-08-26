#include<stdio.h>
#include<conio.h>
#include<string.h>

void main()
{
	char str[100];
	int i,len, flag = 0;
	clrscr();

	printf("\nEnter a string: ");
	gets(str);

	len = strlen(str);

	for(i=0;i<len/2; i++)
	{
		if(str[i] != str[len - i -1])
		{
			flag = 1;
			break;
		}
	}

	if(flag == 0)
		printf("\nPalindrome string");
	else
		printf("\nNot a Palindrome");

	getch();
}
