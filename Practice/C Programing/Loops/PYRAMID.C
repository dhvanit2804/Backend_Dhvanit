#include<stdio.h>
#include<conio.h>

void main()
{
	int i,j,k;
	clrscr();
	for(i=0;i<10;i++)
	{
		for(j=0;j<9-i;j++)
		{
			printf(" ");
		}
		for(k=0;k<i;k++)
		{
			printf(" *");
		}
		printf("\n");
	}
	getch();
}