#include<stdio.h>
#include<conio.h>

void main()
{
	int a;
	clrscr();
	printf("\nEnter A : ");
	scanf("%d",&a);
	if(a%2==0)
	{
		printf("\n%d is Even",a);
	}
	else
	{
		printf("\n%d is Odd",a);
	}
	// Positive Negative
	if(a>0)
	{
		printf("\n%d is Positive",a);
	}
	else if(a<0){
		printf("\n%d is Negative",a);
	}
	else{
		printf("\nThe Number is Zero");
	}
	// 3 and 5
	if(a%3==0 && a%5==0){
		printf("\n%d is divided by both 3 and 5",a);
	}
	else{
		printf("\n%d is not divided by both",a);
	}
	getch();
}