#include<stdio.h>
#include<conio.h>

void main()
{
	int n,i;
	clrscr();
	printf("\nEnter N : ");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		if(i%2==0)
		{
			printf("\n%d is Even",i);
		}
	}
	getch();
}