//Reverse Number
#include<stdio.h>
#include<conio.h>

void main()
{
	int num,rev=0,digit;
	clrscr();
	printf("\nEnter num : ");
	scanf("%d",&num);
	while(num!=0)
	{
		digit = num%10;
		rev = rev*10+digit;
		num /= 10;
	}
	printf("Reversed Number = %d",rev);
	getch();
}