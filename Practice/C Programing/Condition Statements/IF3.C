//Check if num is divisble by both 3 and 5
#include<stdio.h>
#include<conio.h>

void main()
{
	int num;
	clrscr();
	printf("\nEnter Number : ");
	scanf("%d",&num);
	if(num%3==0 && num%5==0)
	{
		printf("\nNumber is divisible by both");
	}
	else{
		printf("\Number is not divisible by both");
	}
	getch();
}