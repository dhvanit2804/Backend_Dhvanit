#include<stdio.h>
#include<conio.h>

void main()
{
	int a[10],i;
	clrscr();
	printf("\nEnter a Array Element\n");
	for(i=0;i<10;i++)
	{
		printf("\nEnter %d Element : ",i);
		scanf("%d",&a[i]);
	}
	printf("\nArray Element Are\n");
	for(i=0;i<10;i++)
	{
		printf("\nA[%d] = %d",i,a[i]);
	}
	getch();
}