#include<stdio.h>
#include<conio.h>

void main()
{
	int a,b;
	clrscr();
	printf("\nEnter A : ");
	scanf("%d",&a);
	printf("\nEnter B : ");
	scanf("%d",&b);
	printf("\nSum = %d", a + b);
	printf("\nSub = %d", a - b);
	printf("\nMul = %d", a * b);
	if(b==0){
		printf("\n0 is not Valid");
	}
	else{
		printf("\nDiv = %d", a / b);
	}
	getch();
}